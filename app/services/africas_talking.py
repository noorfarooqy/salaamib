from datetime import datetime
import aiohttp
from typing import Optional, List, Dict, Union
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.core.config import settings
from app.models.notification import EasyNotification, EasySmsNotification

class AfricasTalkingService:
    def __init__(self, db: Session):
        self.db = db
        self.error = None
        self.success = None
        self.has_failed = False

    async def get_authentication_token(self) -> Optional[EasyNotification]:
        """Get a valid authentication token or create a new one"""
        try:
            # Check for valid token
            token = self.db.query(EasyNotification).filter(
                and_(
                    EasyNotification.at_token.isnot(None),
                    EasyNotification.has_expired == False,
                    EasyNotification.expires_at > datetime.utcnow()
                )
            ).first()

            if token:
                return token

            # If no valid token, create new one
            auth_endpoint = settings.AT_AUTH_ENDPOINT
            uri = f"{settings.AT_API_URL}{auth_endpoint}"

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    uri,
                    headers={
                        "apiKey": settings.AT_API_KEY,
                        "Accept": "application/json",
                        "Content-Type": "application/json",
                        "Host": settings.AT_API_HOST
                    },
                    json={
                        "username": settings.AT_USERNAME
                    }
                ) as response:
                    if response.status not in [200, 201]:
                        self.error = await response.text()
                        return None

                    json_response = await response.json()
                    
                    # Create new token
                    token = EasyNotification(
                        at_token=json_response["token"],
                        expires_at=datetime.utcnow().timestamp() + json_response["lifetimeInSeconds"],
                        has_expired=False
                    )
                    self.db.add(token)
                    self.db.commit()
                    self.db.refresh(token)
                    
                    return token

        except Exception as e:
            self.error = str(e)
            return None

    async def send_sms(self, to: str, message: str, user_id: Optional[int] = None) -> Dict[str, Union[bool, str, dict]]:
        """Send SMS using AfricasTalking"""
        try:
            token = await self.get_authentication_token()
            if not token:
                return {
                    "success": False,
                    "error": self.error or "Failed to get authentication token"
                }

            endpoint = f"{settings.AT_API_URL}{settings.AT_SMS_ENDPOINT}"
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    endpoint,
                    headers={
                        "Accept": "application/json",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "authToken": token.at_token,
                        "Host": settings.AT_API_HOST,
                        "Accept-Encoding": "gzip, deflate, br"
                    },
                    data={
                        "to": to,
                        "message": message,
                        "enqueue": 1,
                        "username": settings.AT_USERNAME,
                        "from": settings.AT_FROM
                    }
                ) as response:
                    response_text = await response.text()
                    
                    # Prepare notification data
                    notification_data = {
                        "used_token_id": token.id,
                        "to": to,
                        "content": message,
                        "user_id": user_id,
                        "is_sent": False,
                        "dlr_response": response_text
                    }

                    if response.status in [200, 201]:
                        json_response = await response.json()
                        sms_data = json_response.get("SMSMessageData", {})
                        recipients = sms_data.get("Recipients", [{}])[0]
                        
                        notification_data.update({
                            "is_sent": True,
                            "message_id": recipients.get("messageId")
                        })

                    # Create SMS notification record
                    sms_notification = EasySmsNotification(**notification_data)
                    self.db.add(sms_notification)
                    self.db.commit()
                    self.db.refresh(sms_notification)

                    return {
                        "success": notification_data["is_sent"],
                        "data": sms_notification,
                        "error": None if notification_data["is_sent"] else "Failed to send SMS"
                    }

        except Exception as e:
            self.error = str(e)
            return {
                "success": False,
                "error": self.error,
                "data": None
            }

    async def send_bulk_sms(
        self,
        to_numbers: List[str],
        message: str,
        user_id: Optional[int] = None
    ) -> Dict[str, Union[bool, str, dict]]:
        """Send bulk SMS using AfricasTalking"""
        try:
            if not to_numbers:
                return {
                    "success": False,
                    "error": "No recipient numbers provided"
                }

            max_bulk = settings.AT_MAX_BULK_SMS or 20
            batches = [to_numbers[i:i + max_bulk] for i in range(0, len(to_numbers), max_bulk)]
            
            last_response = None
            for batch in batches:
                to = ",".join(batch)
                last_response = await self.send_sms(to, message, user_id)

            return last_response or {
                "success": False,
                "error": "No messages sent",
                "data": None
            }

        except Exception as e:
            self.error = str(e)
            return {
                "success": False,
                "error": self.error,
                "data": None
            } 