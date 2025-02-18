from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.sql import func
from app.db.base import Base

class EasyNotification(Base):
    __tablename__ = "easy_notifications"

    id = Column(Integer, primary_key=True, index=True)
    at_token = Column(String)
    expires_at = Column(DateTime(timezone=True))
    has_expired = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class EasySmsNotification(Base):
    __tablename__ = "easy_sms_notifications"

    id = Column(Integer, primary_key=True, index=True)
    used_token_id = Column(Integer, ForeignKey("easy_notifications.id"))
    to = Column(String)
    content = Column(Text)
    user_id = Column(Integer, nullable=True)
    is_sent = Column(Boolean, default=False)
    message_id = Column(String, nullable=True)
    dlr_response = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 