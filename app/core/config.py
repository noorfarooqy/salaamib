from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Salaam Internet Banking"
    ENVIRONMENT: str = "production"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    # Core Banking System
    CBS_SOAP_URL: str
    CBS_USERNAME: str
    CBS_PASSWORD: str
    CBS_SOURCE: str = "SMFBPORTAL"
    CBS_UBSCOMP: str = "FCUBS"
    CBS_USERID: str = "USSDSMFB"
    
    # AfricasTalking Configuration
    AT_API_URL: str = "https://api.africastalking.com/version1"
    AT_AUTH_ENDPOINT: str = "/auth-token/generate"
    AT_SMS_ENDPOINT: str = "/messaging"
    AT_API_KEY: str
    AT_USERNAME: str
    AT_API_HOST: str = "api.africastalking.com"
    AT_FROM: Optional[str] = None
    AT_MAX_BULK_SMS: int = 20
    
    # SMS Gateway
    SMS_GATEWAY_URL: Optional[str] = None
    SMS_API_KEY: Optional[str] = None
    
    # Monitoring
    PROMETHEUS_ENABLED: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 