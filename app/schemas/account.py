from pydantic import BaseModel, condecimal
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class TransactionBase(BaseModel):
    transaction_type: str
    amount: condecimal(max_digits=18, decimal_places=2)
    currency: str
    description: str

class TransactionCreate(TransactionBase):
    account_id: int

class TransactionResponse(TransactionBase):
    id: int
    reference: str
    status: str
    transaction_date: datetime
    created_at: datetime

    class Config:
        from_attributes = True

class AccountBase(BaseModel):
    account_number: str
    account_type: str
    currency: str
    status: str

class AccountCreate(AccountBase):
    user_id: int
    balance: condecimal(max_digits=18, decimal_places=2) = Decimal(0)

class AccountResponse(AccountBase):
    id: int
    balance: condecimal(max_digits=18, decimal_places=2)
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class AccountWithTransactions(AccountResponse):
    transactions: List[TransactionResponse]

    class Config:
        from_attributes = True

class TransactionHistoryRequest(BaseModel):
    from_date: datetime
    to_date: datetime

class AccountBalanceResponse(BaseModel):
    account_number: str
    balance: condecimal(max_digits=18, decimal_places=2)
    currency: str 