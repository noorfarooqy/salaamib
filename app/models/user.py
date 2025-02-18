from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cif_number = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    phone_number = Column(String)
    email = Column(String, nullable=True)
    
    # Personal Information
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    title = Column(String, nullable=True)
    short_name = Column(String, nullable=True)
    nationality = Column(String, nullable=True)
    
    # Address Information
    address_line1 = Column(String, nullable=True)
    address_line2 = Column(String, nullable=True)
    address_line3 = Column(String, nullable=True)
    address_line4 = Column(String, nullable=True)
    address_country = Column(String, nullable=True)
    
    # Identification
    unique_id_name = Column(String, nullable=True)  # Type of ID (e.g., National ID, Passport)
    unique_id_value = Column(String, nullable=True)  # ID number
    
    # Customer Classification
    customer_type = Column(String, nullable=True)  # Individual, Corporate, etc.
    category = Column(String, nullable=True)  # Customer category
    
    # Status and Verification
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    cbs_is_verified = Column(Boolean, default=False)
    
    # Timestamps
    last_login = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    cbs_created_at = Column(DateTime(timezone=True), nullable=True)
    cbs_updated_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    accounts = relationship("Account", back_populates="user") 