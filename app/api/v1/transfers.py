from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import uuid
from typing import Optional

from app.core.security import oauth2_scheme, verify_token
from app.db.base import get_db
from app.models.user import User
from app.models.account import Account, Transaction
from app.models.otp import OTP
from app.schemas.transfer import (
    InternalTransferCreate,
    TransferResponse,
    TransferValidation,
    TransferOTPVerify
)
from app.services.cbs import validate_transfer, execute_transfer
from app.services.sms import send_sms

router = APIRouter()

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
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

async def verify_account_ownership(
    account_number: str,
    user: User,
    db: Session
) -> Account:
    account = db.query(Account).filter(
        Account.account_number == account_number,
        Account.user_id == user.id
    ).first()
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Account {account_number} not found or not owned by user"
        )
    
    if account.status != "active":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Account {account_number} is not active"
        )
    
    return account

@router.post("/validate", response_model=TransferValidation)
async def validate_internal_transfer(
    transfer: InternalTransferCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Validate transfer and check if OTP is required"""
    # Verify account ownership
    from_account = await verify_account_ownership(transfer.from_account, current_user, db)
    
    # Validate transfer with CBS
    validation = await validate_transfer(
        transfer.from_account,
        transfer.to_account,
        transfer.amount
    )
    
    if not validation["is_valid"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validation["message"]
        )
    
    # Generate and save OTP if required
    if validation["requires_otp"]:
        otp_code = ''.join(str(uuid.uuid4().int)[:6])
        otp = OTP(
            user_id=current_user.id,
            code=otp_code,
            purpose="transfer",
            expires_at=datetime.utcnow() + timedelta(minutes=5)
        )
        db.add(otp)
        db.commit()
        
        # Send OTP via SMS
        await send_sms(
            phone_number=current_user.phone_number,
            message=f"Your transfer verification code is: {otp_code}"
        )
    
    return TransferValidation(
        requires_otp=validation["requires_otp"],
        reference=validation["reference"],
        message=validation["message"]
    )

@router.post("/internal", response_model=TransferResponse)
async def create_internal_transfer(
    transfer: InternalTransferCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Execute internal transfer between accounts"""
    # Verify account ownership
    from_account = await verify_account_ownership(transfer.from_account, current_user, db)
    
    # Execute transfer through CBS
    result = await execute_transfer(
        from_account=transfer.from_account,
        to_account=transfer.to_account,
        amount=transfer.amount,
        reference=str(uuid.uuid4()),
        description=transfer.description,
        otp=transfer.otp
    )
    
    if result["status"] != "success":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=result["message"]
        )
    
    # Create transaction records
    debit_transaction = Transaction(
        account_id=from_account.id,
        transaction_type="debit",
        amount=transfer.amount,
        currency=from_account.currency,
        description=transfer.description,
        reference=result["transaction_reference"],
        status="completed",
        transaction_date=datetime.utcnow()
    )
    db.add(debit_transaction)
    
    # Update account balance
    from_account.balance -= transfer.amount
    
    # If destination account is local, create credit transaction
    to_account = db.query(Account).filter(
        Account.account_number == transfer.to_account
    ).first()
    
    if to_account:
        credit_transaction = Transaction(
            account_id=to_account.id,
            transaction_type="credit",
            amount=transfer.amount,
            currency=to_account.currency,
            description=transfer.description,
            reference=result["transaction_reference"],
            status="completed",
            transaction_date=datetime.utcnow()
        )
        db.add(credit_transaction)
        to_account.balance += transfer.amount
    
    db.commit()
    
    return TransferResponse(
        reference=result["transaction_reference"],
        from_account=transfer.from_account,
        to_account=transfer.to_account,
        amount=transfer.amount,
        status="completed",
        description=transfer.description,
        transaction_date=datetime.utcnow()
    )

@router.post("/verify-otp", response_model=TransferResponse)
async def verify_transfer_otp(
    verify: TransferOTPVerify,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Verify OTP for transfer"""
    otp = db.query(OTP).filter(
        OTP.user_id == current_user.id,
        OTP.code == verify.otp,
        OTP.purpose == "transfer",
        OTP.is_used == False
    ).first()
    
    if not otp or not otp.is_valid():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or expired OTP"
        )
    
    # Mark OTP as used
    otp.is_used = True
    db.commit()
    
    # Continue with transfer execution
    # This endpoint would be called after validate_internal_transfer
    # with the OTP and reference from the validation step
    return await execute_transfer_with_otp(verify.reference, verify.otp)

def get_pending_transfer(reference: str) -> Optional[InternalTransferCreate]:
    """Get pending transfer from cache/db using reference"""
    # TODO: Implement actual storage/retrieval logic
    # This is a placeholder implementation
    return None

async def execute_transfer_with_otp(reference: str, otp: str) -> TransferResponse:
    """Execute a transfer that was previously validated and requires OTP"""
    # Get pending transfer from cache/db using reference
    transfer = get_pending_transfer(reference)
    
    if not transfer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transfer not found or expired"
        )
    
    return await create_internal_transfer(
        InternalTransferCreate(
            from_account=transfer.from_account,
            to_account=transfer.to_account,
            amount=transfer.amount,
            description=transfer.description,
            otp=otp
        )
    ) 