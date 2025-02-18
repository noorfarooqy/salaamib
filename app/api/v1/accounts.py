from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta

from app.core.security import oauth2_scheme, verify_token
from app.db.base import get_db
from app.services.logger import AccountLogger
from app.models.user import User
from app.models.account import Account, Transaction
from app.schemas.account import (
    AccountResponse,
    AccountWithTransactions,
    TransactionResponse,
    TransactionHistoryRequest,
    AccountBalanceResponse
)
from app.services.cbs import (
    get_account_details as get_cbs_account_details,
    get_transaction_history, get_account_balance as get_cbs_balance
)

# Initialize logger
account_logger = AccountLogger()

router = APIRouter()

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    cif_number = verify_token(token)
    if not cif_number:
        account_logger.error(f"Invalid token for user")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = db.query(User).filter(User.cif_number == cif_number).first()
    if not user:
        account_logger.error(f"User not found for CIF: {cif_number}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.get("/", response_model=List[AccountResponse])
async def get_accounts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all accounts for the current user"""
    # First try to get from CBS
    cbs_accounts = await get_cbs_account_details(current_user.cif_number)
    
    if cbs_accounts and cbs_accounts.get("is_valid") and cbs_accounts.get("accounts"):
        # Sync CBS accounts with local database
        for acc in cbs_accounts["accounts"]:
            db_account = db.query(Account).filter(
                Account.account_number == acc["accountNumber"]
            ).first()
            
            if not db_account:
                db_account = Account(
                    user_id=current_user.id,
                    account_number=acc["accountNumber"],
                    account_type=acc["accountType"],
                    currency=acc["currency"],
                    status=acc["status"]
                )
                db.add(db_account)
            else:
                db_account.status = acc["status"]
        
        db.commit()
    
    # Return accounts from local database
    return db.query(Account).filter(Account.user_id == current_user.id).all()

@router.get("/{account_number}", response_model=AccountWithTransactions)
async def get_account_info(
    account_number: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get detailed account information including recent transactions"""
    account = db.query(Account).filter(
        Account.account_number == account_number,
        Account.user_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    return account

@router.get("/{account_number}/balance", response_model=AccountBalanceResponse)
async def get_account_balance(
    account_number: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get real-time account balance from CBS"""
    # First verify account ownership
    account = db.query(Account).filter(
        Account.account_number == account_number,
        Account.user_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    # Get real-time balance from CBS
    account_logger.info(f"Getting balance for account {account_number}")
    cbs_balance = await get_cbs_balance(account_number)
    if not cbs_balance:
        account_logger.error(f"Failed to get CBS balance for account {account_number}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get account balance from CBS"
        )
    
    # Update local database with CBS balance
    account.balance = cbs_balance["available_balance"]
    account.currency = cbs_balance["currency"]
    db.commit()
    
    return {
        "account_number": account.account_number,
        "balance": cbs_balance["available_balance"],
        "currency": cbs_balance["currency"]
    }

@router.get("/{account_number}/transactions", response_model=List[TransactionResponse])
async def get_account_transactions(
    account_number: str,
    request: TransactionHistoryRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get account transaction history"""
    account = db.query(Account).filter(
        Account.account_number == account_number,
        Account.user_id == current_user.id
    ).first()
    
    if not account:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Account not found"
        )
    
    # Get transactions from CBS
    cbs_transactions = await get_transaction_history(
        account_number,
        request.from_date.strftime("%Y-%m-%d"),
        request.to_date.strftime("%Y-%m-%d")
    )
    
    if cbs_transactions:
        # Sync CBS transactions with local database
        for trans in cbs_transactions:
            db_transaction = db.query(Transaction).filter(
                Transaction.reference == trans["reference"]
            ).first()
            
            if not db_transaction:
                db_transaction = Transaction(
                    account_id=account.id,
                    transaction_type=trans["type"],
                    amount=trans["amount"],
                    currency=trans["currency"],
                    description=trans["description"],
                    reference=trans["reference"],
                    status=trans["status"],
                    transaction_date=datetime.fromisoformat(trans["transactionDate"])
                )
                db.add(db_transaction)
        
        db.commit()
    
    # Return transactions from local database
    return db.query(Transaction).filter(
        Transaction.account_id == account.id,
        Transaction.transaction_date.between(request.from_date, request.to_date)
    ).order_by(Transaction.transaction_date.desc()).all() 