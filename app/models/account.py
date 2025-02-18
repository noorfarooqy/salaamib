from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)  # savings, current, etc.
    currency = Column(String)
    balance = Column(Numeric(precision=18, scale=2))
    status = Column(String)  # active, dormant, closed
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    transaction_type = Column(String)  # credit, debit
    amount = Column(Numeric(precision=18, scale=2))
    currency = Column(String)
    description = Column(String)
    reference = Column(String, unique=True, index=True)
    status = Column(String)  # pending, completed, failed
    transaction_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    account = relationship("Account", back_populates="transactions") 