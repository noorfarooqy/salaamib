from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.core.config import settings
from app.services.logger import DBLogger, ErrorLogger 
from typing import Generator

# Create database engine
engine = create_engine(settings.DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class
Base = declarative_base()
db_logger = DBLogger()
error_logger = ErrorLogger()

def get_db() -> Generator:
    """Database dependency that ensures proper session management"""
    db = SessionLocal()
    try:
        db_logger.info("Opening new database connection")
        yield db
    except Exception as e:
        error_logger.error(f"Database error: {str(e)}", exc_info=True)
        raise
    finally:
        db_logger.info("Closing database connection")
        db.close()