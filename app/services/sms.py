from typing import Optional
from sqlalchemy.orm import Session
from app.services.africas_talking import AfricasTalkingService
from app.db.base import get_db
from app.core.config import settings

class SMSService:
    def __init__(self, db: Session):
        self.db = db
        self.at_service = AfricasTalkingService(db)

    async def send_sms(self, phone_number: str, message: str, user_id: Optional[int] = None) -> bool:
        """
        Send SMS using AfricasTalking
        In development mode, just print the message and return success
        """
        try:
            if settings.ENVIRONMENT == "development":
                print(f"[DEV MODE] SMS to {phone_number}: {message}")
                return True
                
            result = await self.at_service.send_sms(phone_number, message, user_id)
            return result["success"]
        except Exception as e:
            print(f"Error sending SMS: {str(e)}")
            return False

    async def send_bulk_sms(self, phone_numbers: list[str], message: str, user_id: Optional[int] = None) -> bool:
        """
        Send bulk SMS using AfricasTalking
        In development mode, just print the messages and return success
        """
        try:
            if settings.ENVIRONMENT == "development":
                for phone in phone_numbers:
                    print(f"[DEV MODE] SMS to {phone}: {message}")
                return True
                
            result = await self.at_service.send_bulk_sms(phone_numbers, message, user_id)
            return result["success"]
        except Exception as e:
            print(f"Error sending bulk SMS: {str(e)}")
            return False

# Create singleton instance
sms_service = SMSService(next(get_db()))

# Export send_sms function
async def send_sms(phone_number: str, message: str, user_id: Optional[int] = None) -> bool:
    """Send SMS using the SMS service"""
    return await sms_service.send_sms(phone_number, message, user_id) 