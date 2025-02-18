from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from app.db.base import Base
from datetime import datetime
import pytz

class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    code = Column(String)
    purpose = Column(String)  # registration, login, transaction
    is_used = Column(Boolean, default=False)
    expires_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def is_valid(self) -> bool:
        """Check if OTP is valid (not used and not expired)"""
        now = datetime.now(pytz.UTC)
        return not self.is_used and self.expires_at > now 