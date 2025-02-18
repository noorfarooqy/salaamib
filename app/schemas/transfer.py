from pydantic import BaseModel, condecimal, Field
from typing import Optional
from decimal import Decimal
from datetime import datetime

class TransferBase(BaseModel):
    from_account: str
    to_account: str
    amount: condecimal(max_digits=18, decimal_places=2, gt=Decimal(0))
    description: str = Field(..., min_length=3, max_length=100)

class InternalTransferCreate(TransferBase):
    otp: Optional[str] = None  # Required for amounts above threshold

class TransferResponse(BaseModel):
    reference: str
    from_account: str
    to_account: str
    amount: condecimal(max_digits=18, decimal_places=2)
    status: str
    description: str
    transaction_date: datetime
    
    class Config:
        from_attributes = True

class TransferValidation(BaseModel):
    requires_otp: bool
    reference: str  # Used to link OTP verification with transfer
    message: str

class TransferOTPVerify(BaseModel):
    reference: str
    otp: str 