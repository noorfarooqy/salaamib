from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, UTC
import random
import string
import logging
import pytz
from typing import Dict, Any, Optional
import uuid

from app.services.logger import AuthLogger

from app.core.security import verify_password, get_password_hash, create_access_token, verify_token, oauth2_scheme
from app.db.base import get_db
from app.models.user import User
from app.models.otp import OTP
from app.models.account import Account
from app.schemas.user import UserCreate, UserVerify, UserLogin, UserResponse, Token, ResendOTP, ForgotPassword, ResetPassword
from app.services.cbs import verify_cif
from app.services.sms import send_sms
from app.services.crud import user as crud_user, account as crud_account
from app.schemas.account import AccountCreate
from app.utils.exceptions import ValidationError

router = APIRouter()
auth_logger = AuthLogger()

# Constants for login security
MAX_LOGIN_ATTEMPTS = 5
LOCKOUT_DURATION_MINUTES = 30

# Constants for OTP security
MAX_OTP_ATTEMPTS = 3
OTP_LOCKOUT_DURATION_MINUTES = 15

def generate_otp(length: int = 6) -> str:
    return ''.join(random.choices(string.digits, k=length))

@router.post("/register", response_model=dict)
async def register(
    request: Request,
    cif_number: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
) -> Dict[str, Any]:
    """Register a new user"""
    try:
        # Verify CIF with CBS first
        cbs_validation = await verify_cif(cif_number)
        
        if not cbs_validation["is_valid"]:
            raise HTTPException(
                status_code=400,
                detail=cbs_validation["error"]
            )

        # Check if user already exists
        user = crud_user.get_by_cif(db, cif_number=cif_number)
        if user:
            raise HTTPException(
                status_code=400,
                detail="User already registered"
            )
        auth_logger.log_info(f"cbs validation: {cbs_validation}")

        # Create user object with CBS fields
        user_in = UserCreate(
            cif_number=cif_number,
            password=password,
            phone_number=cbs_validation.get("mobile", ""),
            email=cbs_validation.get("email"),
            first_name=cbs_validation.get("first_name"),
            last_name=cbs_validation.get("last_name"),
            gender=cbs_validation.get("gender"),
            title=cbs_validation.get("title"),
            short_name=cbs_validation.get("short_name"),
            nationality=cbs_validation.get("nationality"),
            address_line1=cbs_validation.get("address_line1"),
            address_line2=cbs_validation.get("address_line2"),
            address_line3=cbs_validation.get("address_line3"),
            address_line4=cbs_validation.get("address_line4"),
            address_country=cbs_validation.get("address_country"),
            unique_id_name=cbs_validation.get("unique_id_name"),
            unique_id_value=cbs_validation.get("unique_id_value"),
            customer_type=cbs_validation.get("customer_type"),
            category=cbs_validation.get("category")
        )

        # Create user in database
        user = crud_user.create(db, obj_in=user_in)
        
        # Create accounts
        for account in cbs_validation["accounts"]:
            account_in = AccountCreate(
                account_number=account["accountNumber"],
                account_type=account["accountType"],
                currency=account["currency"],
                status=account["status"],
                user_id=user.id
            )
            crud_account.create(db, obj_in=account_in)

        # Generate OTP for registration verification
        otp_code = generate_otp()
        otp = OTP(
            user_id=user.id,
            code=otp_code,
            purpose="registration",
            expires_at=datetime.now(pytz.UTC) + timedelta(minutes=5)
        )
        db.add(otp)
        db.commit()

        # Send OTP via SMS
        await send_sms(
            phone_number=user.phone_number,
            message=f"Your Salaam IB verification code is: {otp_code}"
        )

        return {
            "status": "success",
            "message": "Registration successful. Please verify your account with the OTP sent to your phone.",
            "user_id": user.id
        }

    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        auth_logger.log_error(f"Registration error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during registration: {str(e)}"
        )

@router.post("/verify", response_model=Token)
async def verify_registration(user_verify: UserVerify, db: Session = Depends(get_db)):
    auth_logger.log_info(f"Verifying registration for CIF: {user_verify.cif_number}")
    
    user = db.query(User).filter(User.cif_number == user_verify.cif_number).first()
    if not user:
        auth_logger.log_error(f"User not found with CIF: {user_verify.cif_number}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if user is OTP locked
    now = datetime.now(pytz.UTC)
    if user.otp_locked_until and user.otp_locked_until > now:
        lock_remaining = int((user.otp_locked_until - now).total_seconds() / 60)
        auth_logger.log_error(f"OTP verification locked for user {user.cif_number}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Too many failed attempts. Please try again in {lock_remaining} minutes"
        )
    
    # Reset OTP attempts if lock has expired
    if user.otp_locked_until and user.otp_locked_until <= now:
        user.otp_attempts = 0
        user.otp_locked_until = None
    
    auth_logger.log_info(f"Found user with ID: {user.id}")
    otp = db.query(OTP).filter(
        OTP.user_id == user.id,
        OTP.purpose == "registration",
        OTP.is_used == False
    ).order_by(OTP.created_at.desc()).first()
    
    if not otp:
        auth_logger.log_error(f"No unused OTP found for user ID: {user.id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    auth_logger.log_info(f"Found OTP record: valid until {otp.expires_at}, is_used: {otp.is_used}")
    if not otp.is_valid():
        auth_logger.log_error(f"OTP is not valid. Expires at: {otp.expires_at}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    if otp.code != user_verify.otp:
        # Increment OTP attempts
        user.otp_attempts += 1
        
        # Check if max attempts reached
        if user.otp_attempts >= MAX_OTP_ATTEMPTS:
            user.otp_locked_until = now + timedelta(minutes=OTP_LOCKOUT_DURATION_MINUTES)
            db.commit()
            auth_logger.log_error(f"OTP verification locked for user {user.cif_number}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Too many failed attempts. Please try again in {OTP_LOCKOUT_DURATION_MINUTES} minutes"
            )
            
        remaining_attempts = MAX_OTP_ATTEMPTS - user.otp_attempts
        db.commit()
        auth_logger.log_error(f"OTP code mismatch. Expected: {otp.code}, Got: {user_verify.otp}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid OTP. {remaining_attempts} attempts remaining"
        )
    
    # Reset OTP attempts on successful verification
    user.otp_attempts = 0
    user.otp_locked_until = None
    
    # Mark OTP as used and user as verified
    otp.is_used = True
    user.is_verified = True
    db.commit()
    auth_logger.log_info(f"User {user.cif_number} verified successfully")
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user.cif_number}
    )
    
    # Convert User model to UserResponse schema
    user_response = UserResponse(
        id=user.id,
        cif_number=user.cif_number,
        phone_number=user.phone_number,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        gender=user.gender,
        title=user.title,
        short_name=user.short_name,
        nationality=user.nationality,
        address_line1=user.address_line1,
        address_line2=user.address_line2,
        address_line3=user.address_line3,
        address_line4=user.address_line4,
        address_country=user.address_country,
        unique_id_name=user.unique_id_name,
        unique_id_value=user.unique_id_value,
        customer_type=user.customer_type,
        category=user.category,
        is_active=user.is_active,
        is_verified=user.is_verified,
        last_login=user.last_login,
        created_at=user.created_at
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user_response
    }

@router.post("/login", response_model=Dict[str, Any])
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """Login user with CIF number and password"""
    try:
        user = db.query(User).filter(User.cif_number == form_data.username).first()
        
        # Check if user exists
        if not user:
            auth_logger.log_error(f"Login failed: User not found for CIF {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid CIF number or password"
            )
            
        # Check if user is verified
        if not user.is_verified:
            auth_logger.log_error(f"Login attempt by unverified user: {form_data.username}")
            # Generate new OTP for verification
            otp_code = generate_otp()
            otp = OTP(
                user_id=user.id,
                code=otp_code,
                purpose="registration",
                expires_at=datetime.now(pytz.UTC) + timedelta(minutes=5)
            )
            db.add(otp)
            
            # Mark all previous unused registration OTPs as used
            old_otps = db.query(OTP).filter(
                OTP.user_id == user.id,
                OTP.purpose == "registration",
                OTP.is_used == False
            ).all()
            for old_otp in old_otps:
                old_otp.is_used = True
            
            db.commit()
            
            # Send new OTP via SMS
            await send_sms(
                phone_number=user.phone_number,
                message=f"Your Salaam IB verification code is: {otp_code}"
            )
            
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Account not verified. A new verification code has been sent to your phone."
            )
            
        # Check if account is locked
        now = datetime.now(pytz.UTC)
        if user.is_locked and user.locked_until and user.locked_until > now:
            remaining_time = int((user.locked_until - now).total_seconds() / 60)
            auth_logger.log_info(f"Login attempt for locked account: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Account is locked. Please try again after {remaining_time} minutes"
            )
            
        # Reset lock if lockout period has expired
        if user.is_locked and user.locked_until and user.locked_until <= now:
            user.is_locked = False
            user.login_attempts = 0
            user.locked_until = None
            db.commit()
            
        # Verify password
        if not verify_password(form_data.password, user.hashed_password):
            # Increment login attempts
            user.login_attempts += 1
            
            # Check if max attempts reached
            if user.login_attempts >= MAX_LOGIN_ATTEMPTS:
                user.is_locked = True
                user.locked_until = now + timedelta(minutes=LOCKOUT_DURATION_MINUTES)
                db.commit()
                
                auth_logger.log_info(f"Account locked due to max login attempts: {form_data.username}")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=f"Account has been locked for {LOCKOUT_DURATION_MINUTES} minutes due to too many failed attempts"
                )
                
            db.commit()
            remaining_attempts = MAX_LOGIN_ATTEMPTS - user.login_attempts
            auth_logger.log_info(f"Failed login attempt {user.login_attempts} for user {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid CIF number or password. {remaining_attempts} attempts remaining"
            )
            
        # Check if user is active
        if not user.is_active:
            auth_logger.log_error(f"Login attempt for inactive account: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Account is inactive"
            )
            
        # Generate OTP for 2FA
        otp_code = ''.join(str(uuid.uuid4().int)[:6])
        otp = OTP(
            user_id=user.id,
            code=otp_code,
            purpose="2fa_login",
            expires_at=datetime.now(pytz.UTC) + timedelta(minutes=5)
        )
        db.add(otp)
        
        # Reset login attempts on successful password verification
        user.login_attempts = 0
        user.is_locked = False
        user.locked_until = None
        db.commit()
        
        # Send OTP via SMS
        await send_sms(
            phone_number=user.phone_number,
            message=f"Your login verification code is: {otp_code}"
        )
        
        auth_logger.log_info(f"2FA OTP sent for user {form_data.username}")
        return {
            "requires_2fa": True,
            "cif_number": user.cif_number,
            "message": "Please enter the verification code sent to your phone"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        auth_logger.log_error(f"Login error for {form_data.username}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed"
        )

@router.post("/verify-2fa", response_model=Token)
async def verify_2fa(
    cif_number: str = Form(...),
    otp: str = Form(...),
    db: Session = Depends(get_db)
):
    """Second step of 2FA login - verify OTP and return access token"""
    try:
        user = db.query(User).filter(User.cif_number == cif_number).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Check if user is OTP locked
        now = datetime.now(pytz.UTC)
        if user.otp_locked_until and user.otp_locked_until > now:
            lock_remaining = int((user.otp_locked_until - now).total_seconds() / 60)
            auth_logger.log_error(f"OTP verification locked for user {cif_number}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Too many failed attempts. Please try again in {lock_remaining} minutes"
            )

        # Reset OTP attempts if lock has expired
        if user.otp_locked_until and user.otp_locked_until <= now:
            user.otp_attempts = 0
            user.otp_locked_until = None

        # Verify OTP
        otp_record = db.query(OTP).filter(
            OTP.user_id == user.id,
            OTP.code == otp,
            OTP.purpose == "2fa_login",
            OTP.is_used == False
        ).first()

        if not otp_record or not otp_record.is_valid():
            # Increment OTP attempts
            user.otp_attempts += 1
            
            # Check if max attempts reached
            if user.otp_attempts >= MAX_OTP_ATTEMPTS:
                user.otp_locked_until = now + timedelta(minutes=OTP_LOCKOUT_DURATION_MINUTES)
                db.commit()
                auth_logger.log_error(f"OTP verification locked for user {cif_number}")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Too many failed attempts. Please try again in {OTP_LOCKOUT_DURATION_MINUTES} minutes"
                )
                
            remaining_attempts = MAX_OTP_ATTEMPTS - user.otp_attempts
            db.commit()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid or expired 2FA code. {remaining_attempts} attempts remaining"
            )

        # Reset OTP attempts on successful verification
        user.otp_attempts = 0
        user.otp_locked_until = None

        # Mark OTP as used and update last login
        otp_record.is_used = True
        user.last_login = datetime.now(UTC)
        db.commit()

        # Create access token
        access_token = create_access_token(
            data={"sub": user.cif_number}
        )
        
        auth_logger.log_info(f"2FA verification successful for CIF: {cif_number}")
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user
        }

    except HTTPException:
        raise
    except Exception as e:
        auth_logger.log_error(f"2FA verification failed for {cif_number}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to verify 2FA code"
        )

@router.get("/profile", response_model=UserResponse)
async def get_profile(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Get user profile information"""
    try:
        cif_number = verify_token(token)
        if not cif_number:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )

        user = db.query(User).filter(User.cif_number == cif_number).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        auth_logger.log_info(f"Profile retrieved for user {cif_number}")
        return user
        
    except Exception as e:
        auth_logger.log_error(f"Profile retrieval failed for {cif_number}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve profile"
        )

@router.post("/resend-otp", response_model=dict)
async def resend_otp(resend_request: ResendOTP, db: Session = Depends(get_db)):
    """Resend OTP for unverified users"""
    auth_logger.log_info(f"Resending OTP for CIF: {resend_request.cif_number}")
    
    # Find the user
    user = db.query(User).filter(User.cif_number == resend_request.cif_number).first()
    if not user:
        auth_logger.log_error(f"User not found with CIF: {resend_request.cif_number}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Check if user is already verified
    if user.is_verified:
        auth_logger.log_error(f"User {user.cif_number} is already verified")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User is already verified. Please login."
        )
    
    # Generate new OTP
    otp_code = generate_otp()
    now = datetime.now(pytz.UTC)
    otp = OTP(
        user_id=user.id,
        code=otp_code,
        purpose="registration",
        expires_at=now + timedelta(minutes=5)
    )
    db.add(otp)
    
    # Mark all previous unused OTPs as used
    old_otps = db.query(OTP).filter(
        OTP.user_id == user.id,
        OTP.purpose == "registration",
        OTP.is_used == False
    ).all()
    for old_otp in old_otps:
        old_otp.is_used = True
    
    db.commit()
    
    # Send new OTP via SMS
    await send_sms(
        phone_number=user.phone_number,
        message=f"Your new Salaam IB verification code is: {otp_code}"
    )
    
    auth_logger.log_info(f"New OTP sent to user {user.cif_number}")
    return {"message": "New verification code has been sent to your phone."}

@router.post("/forgot-password", response_model=Dict[str, str])
async def forgot_password(
    request: ForgotPassword,
    db: Session = Depends(get_db)
):
    """Initiate forgot password process"""
    try:
        user = db.query(User).filter(User.cif_number == request.cif_number).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Generate OTP
        otp_code = ''.join(str(uuid.uuid4().int)[:6])
        otp = OTP(
            user_id=user.id,
            code=otp_code,
            purpose="reset_password",
            expires_at=datetime.now(pytz.UTC) + timedelta(minutes=5)
        )
        db.add(otp)
        db.commit()

        # Send OTP via SMS
        await send_sms(
            phone_number=user.phone_number,
            message=f"Your password reset code is: {otp_code}"
        )

        auth_logger.log_info(f"Password reset OTP sent for user {request.cif_number}")
        return {"message": "Password reset OTP has been sent to your registered phone number"}

    except Exception as e:
        auth_logger.log_error(f"Password reset failed for {request.cif_number}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process password reset request"
        )

@router.post("/reset-password", response_model=Dict[str, str])
async def reset_password(
    reset_data: ResetPassword,
    db: Session = Depends(get_db)
):
    """Reset password with OTP verification"""
    try:
        user = db.query(User).filter(User.cif_number == reset_data.cif_number).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        auth_logger.log_info(f"Resetting password for user with id {user.id} with OTP: {reset_data.otp} and new password: {reset_data.new_password}")

        # Verify OTP
        otp = db.query(OTP).filter(
            OTP.user_id == user.id,
            OTP.code == reset_data.otp,
            OTP.purpose == "reset_password",
            OTP.is_used == False
        ).first()

        if not otp :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired OTP "
            )
        if not otp.is_valid():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Expired or invalid OTP "
            )

        # Update password
        user.hashed_password = get_password_hash(reset_data.new_password)
        otp.is_used = True
        db.commit()

        auth_logger.log_info(f"Password reset successful for user {reset_data.cif_number}")
        return {"message": "Password has been reset successfully"}

    except Exception as e:
        auth_logger.log_error(f"Password reset failed for {reset_data.cif_number}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to reset password {str(e)}"
        )

@router.post("/resend-2fa", response_model=Dict[str, str])
async def resend_2fa(
    cif_number: str = Form(...),
    db: Session = Depends(get_db)
):
    """Resend 2FA OTP for login"""
    try:
        user = db.query(User).filter(User.cif_number == cif_number).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # Generate new OTP
        otp_code = ''.join(str(uuid.uuid4().int)[:6])
        otp = OTP(
            user_id=user.id,
            code=otp_code,
            purpose="2fa_login",
            expires_at=datetime.now(UTC) + timedelta(minutes=5)
        )
        db.add(otp)

        # Mark all previous unused 2FA OTPs as used
        old_otps = db.query(OTP).filter(
            OTP.user_id == user.id,
            OTP.purpose == "2fa_login",
            OTP.is_used == False
        ).all()
        for old_otp in old_otps:
            old_otp.is_used = True

        db.commit()

        # Send new OTP via SMS
        await send_sms(
            phone_number=user.phone_number,
            message=f"Your login verification code is: {otp_code}"
        )

        auth_logger.log_info(f"2FA OTP resent for user {cif_number}")
        return {"message": "New verification code has been sent to your phone"}

    except Exception as e:
        auth_logger.log_error(f"Failed to resend 2FA OTP for {cif_number}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to resend verification code"
        ) 