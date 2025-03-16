from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    cif_number: str
    phone_number: str
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    title: Optional[str] = None
    short_name: Optional[str] = None
    nationality: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_line3: Optional[str] = None
    address_line4: Optional[str] = None
    address_country: Optional[str] = None
    unique_id_name: Optional[str] = None
    unique_id_value: Optional[str] = None
    customer_type: Optional[str] = None
    category: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDBBase(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    cbs_is_verified: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    cbs_created_at: Optional[datetime] = None
    cbs_updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass

class UserInDB(UserInDBBase):
    hashed_password: str

class UserVerify(BaseModel):
    cif_number: str
    otp: str

class ResendOTP(BaseModel):
    cif_number: str

class UserLogin(BaseModel):
    cif_number: str
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    last_login: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

class TokenData(BaseModel):
    cif_number: str

class ForgotPassword(BaseModel):
    cif_number: str

class ResetPassword(BaseModel):
    cif_number: str
    otp: str
    new_password: str 