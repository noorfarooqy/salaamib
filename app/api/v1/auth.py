from fastapi import APIRouter, Depends, HTTPException, status, Request, Form
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
import string
import logging
import pytz
from typing import Dict, Any

from app.services.logger import AuthLogger

from app.core.security import verify_password, get_password_hash, create_access_token, verify_token, oauth2_scheme
from app.db.base import get_db
from app.models.user import User
from app.models.otp import OTP
from app.models.account import Account
from app.schemas.user import UserCreate, UserVerify, UserLogin, UserResponse, Token, ResendOTP
from app.services.cbs import verify_cif
from app.services.sms import send_sms
from app.services.crud import user as crud_user, account as crud_account
from app.schemas.account import AccountCreate
from app.utils.exceptions import ValidationError

router = APIRouter()
auth_logger = AuthLogger()


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

        return {
            "status": "success",
            "message": "Registration successful",
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
        auth_logger.log_error(f"OTP code mismatch. Expected: {otp.code}, Got: {user_verify.otp}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Mark OTP as used and user as verified
    otp.is_used = True
    user.is_verified = True
    db.commit()
    auth_logger.log_info(f"User {user.cif_number} verified successfully")
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user.cif_number}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    try:
        auth_logger.log_info(f"Login attempt for CIF: {form_data.username}")
        
        # Check if user exists
        user = db.query(User).filter(User.cif_number == form_data.username).first()
        if not user:
            auth_logger.log_error(f"User not found with CIF: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect CIF number or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Verify password
        if not verify_password(form_data.password, user.hashed_password):
            auth_logger.log_error(f"Invalid password for CIF: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect CIF number or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is verified
        if not user.is_verified:
            auth_logger.log_error(f"Unverified user attempt to login: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Please verify your account first",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Update last login
        user.last_login = datetime.now(pytz.UTC)
        db.commit()
        
        # Create access token
        access_token = create_access_token(
            data={"sub": user.cif_number}
        )
        auth_logger.log_info(f"Login successful for CIF: {form_data.username}")
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        auth_logger.log_error(f"Login error for CIF {form_data.username}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during login"
        )

@router.get("/me", response_model=UserResponse)
async def read_users_me(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
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
    
    return user

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