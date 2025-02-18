import logging
import os
from pathlib import Path
from datetime import datetime

# Create logs directory if it doesn't exist
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

class BaseLogger:
    """Base logger class with common configuration"""
    def __init__(self, name: str, log_file_prefix: str):
        self.name = name
        self.log_file_prefix = log_file_prefix
        self.logger = None
        self._setup_logger()
    
    def _get_log_filename(self):
        """Get log filename with current date"""
        today = datetime.now().strftime('%Y-%m-%d')
        return f"{self.log_file_prefix}_{today}.log"
        
    def _setup_logger(self):
        """Setup logger with current date's log file"""
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        
        # Remove existing handlers
        self.logger.handlers = []
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Create file handler with current date's log file
        log_file = os.path.join(logs_dir, self._get_log_filename())
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        
        # Add handler
        self.logger.addHandler(file_handler)

    def log_info(self, message: str):
        """Log info level message"""
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(message)

class CBSLogger(BaseLogger):
    """Logger for CBS related operations"""
    def __init__(self):
        super().__init__('cbs', 'cbs')
    
    def log_request(self, service: str, operation: str, payload: dict):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(f"CBS Request - Service: {service}, Operation: {operation}, Payload: {payload}")
        
    def log_response(self, response: dict):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(f"Parsed CBS response body: {response}")
        
    def log_error(self, error: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.error(f"CBS Error: {error}")

class AuthLogger(BaseLogger):
    """Logger for authentication related operations"""
    def __init__(self):
        super().__init__('auth', 'auth')
    
    def log_login(self, user_id: str, status: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(f"Login attempt - User: {user_id}, Status: {status}")
        
    def log_logout(self, user_id: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(f"User logged out: {user_id}")
        
    def log_error(self, error: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.error(f"Auth Error: {error}")

class TransactionLogger(BaseLogger):
    """Logger for financial transactions"""
    def __init__(self):
        super().__init__('transaction', 'transactions')
    
    def log_transaction(self, transaction_id: str, transaction_type: str, amount: float, status: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.info(
            f"Transaction - ID: {transaction_id}, Type: {transaction_type}, "
            f"Amount: {amount}, Status: {status}"
        )
        
    def log_error(self, transaction_id: str, error: str):
        self._setup_logger()  # Ensure using current date's log file
        self.logger.error(f"Transaction Error - ID: {transaction_id}, Error: {error}")

class DBLogger(BaseLogger):
    """Logger for database operations"""
    def __init__(self):
        super().__init__('db', 'db')
    
    def info(self, message: str):
        self._setup_logger()
        self.logger.info(message)
        
    def error(self, message: str):
        self._setup_logger()
        self.logger.error(message)

class ErrorLogger(BaseLogger):
    """Logger for general error handling"""
    def __init__(self):
        super().__init__('error', 'error')
    
    def error(self, message: str, exc_info=False):
        self._setup_logger()
        self.logger.error(message, exc_info=exc_info)

class AccountLogger(BaseLogger):
    """Logger for account related operations"""
    def __init__(self):
        super().__init__('account', 'account')
    
    def info(self, message: str):
        self._setup_logger()
        self.logger.info(message)
        
    def error(self, message: str):
        self._setup_logger()
        self.logger.error(message)

# Create logger instances
cbs_logger = CBSLogger()
auth_logger = AuthLogger()
transaction_logger = TransactionLogger()
db_logger = DBLogger()
error_logger = ErrorLogger()
account_logger = AccountLogger()
