# Salaam Internet Banking System - Technical Documentation

## System Overview
The Salaam Internet Banking System is a robust, secure, and scalable solution integrated with Flexcube 14.3 Core Banking System (CBS). The system is built using modern technologies and follows best practices in software development, security, and system architecture.

## Architecture

### Backend Stack
- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT + OTP
- **Caching**: Redis
- **Task Queue**: Celery
- **API Documentation**: OpenAPI (Swagger)
- **SMS Gateway**: Africa's Talking API
- **Core Banking Integration**: SOAP XML via Flexcube 14.3

### Directory Structure
```
salaam-ib/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py         # Authentication endpoints
│   │       ├── accounts.py     # Account management endpoints
│   │       └── transfers.py    # Fund transfer endpoints
│   ├── core/
│   │   ├── config.py          # Application configuration
│   │   └── security.py        # Security utilities
│   ├── db/
│   │   └── base.py           # Database configuration
│   ├── models/               # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   └── services/           # Business logic services
├── scripts/               # Utility scripts
└── alembic/              # Database migrations
```

## Core Components

### 1. Authentication System (`app/api/v1/auth.py`)
- Implements user registration and authentication
- Features:
  - CIF number validation with CBS
  - Password hashing using bcrypt
  - JWT token generation
  - OTP verification via SMS
  - Session management

### 2. Account Management (`app/api/v1/accounts.py`)
- Handles account-related operations
- Features:
  - Account listing and details
  - Balance inquiry
  - Transaction history
  - Real-time CBS synchronization

### 3. Fund Transfer System (`app/api/v1/transfers.py`)
- Manages internal fund transfers
- Features:
  - Transfer validation
  - OTP verification for large amounts
  - CBS integration for execution
  - Transaction logging

### 4. Core Banking Integration (`app/services/cbs.py`)
- Handles all CBS interactions
- Features:
  - SOAP XML request generation
  - Response parsing
  - Error handling
  - Automatic retries
  - Transaction validation

### 5. SMS Notification System (`app/services/africas_talking.py`)
- Manages SMS communications
- Features:
  - OTP delivery
  - Transaction notifications
  - Token management
  - Bulk SMS support

## Database Models

### 1. User Model (`app/models/user.py`)
```python
class User:
    - id: Primary key
    - cif_number: Unique customer identifier
    - personal_info: Name, gender, etc.
    - contact_info: Phone, email
    - address_info: Multiple address lines
    - status_flags: active, verified, etc.
```

### 2. Account Model (`app/models/account.py`)
```python
class Account:
    - id: Primary key
    - user_id: Foreign key to User
    - account_number: Unique identifier
    - type: savings/current
    - currency: Account currency
    - balance: Current balance
    - status: active/dormant/closed
```

### 3. Transaction Model (`app/models/account.py`)
```python
class Transaction:
    - id: Primary key
    - account_id: Foreign key to Account
    - type: credit/debit
    - amount: Transaction amount
    - reference: Unique reference
    - status: pending/completed/failed
```

### 4. OTP Model (`app/models/otp.py`)
```python
class OTP:
    - id: Primary key
    - user_id: Foreign key to User
    - code: OTP code
    - purpose: registration/transfer
    - expires_at: Expiration timestamp
```

### 5. Notification Model (`app/models/notification.py`)
```python
class EasySmsNotification:
    - id: Primary key
    - to: Recipient number
    - content: Message content
    - status: sent/failed
    - message_id: Provider reference
```

## Utility Scripts

### 1. Transaction Creator (`scripts/create_transaction.py`)
- Creates transactions in CBS
- Features:
  - Batch processing
  - M-PESA charge calculation
  - Commission handling
  - Error logging

### 2. Transaction Reversal (`scripts/reverse_transaction.py`)
- Reverses transactions in CBS
- Features:
  - Batch processing
  - Response validation
  - Detailed logging
  - Error handling

## Security Features

1. **Authentication**
   - JWT-based token authentication
   - OTP verification for sensitive operations
   - Password hashing using bcrypt
   - Token expiration and refresh

2. **Data Protection**
   - HTTPS enforcement
   - Input validation using Pydantic
   - SQL injection prevention via SQLAlchemy
   - XSS protection

3. **Access Control**
   - Role-based access control
   - Account ownership validation
   - Transaction amount limits
   - IP-based rate limiting

## Configuration

### Environment Variables (`app/core/config.py`)
- Application settings
- Database configuration
- CBS connection details
- SMS gateway credentials
- Security parameters

### Database Configuration (`alembic.ini`)
- Database connection settings
- Migration configuration
- Logging settings

## API Documentation

### Authentication Endpoints
- POST `/api/v1/auth/register`: Register new user
- POST `/api/v1/auth/verify`: Verify registration OTP
- POST `/api/v1/auth/login`: User login
- GET `/api/v1/auth/me`: Get user profile

### Account Endpoints
- GET `/api/v1/accounts`: List user accounts
- GET `/api/v1/accounts/{number}`: Get account details
- GET `/api/v1/accounts/{number}/balance`: Get real-time balance
- GET `/api/v1/accounts/{number}/transactions`: Get transaction history

### Transfer Endpoints
- POST `/api/v1/transfers/validate`: Validate transfer
- POST `/api/v1/transfers/internal`: Execute transfer
- POST `/api/v1/transfers/verify-otp`: Verify transfer OTP

## Error Handling
- Custom exception classes
- Detailed error logging
- User-friendly error messages
- CBS error mapping

## Logging
- Structured logging format
- Separate logs for different components
- Error tracking
- Transaction audit trail

## Development Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
4. Initialize database:
   ```bash
   alembic upgrade head
   ```
5. Run development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## Production Deployment

1. Build Docker image:
   ```bash
   docker build -t salaam-ib .
   ```
2. Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```

## Monitoring
- Prometheus metrics
- Error rate monitoring
- Transaction success rate
- API response times
- System resource usage

## Future Improvements
1. Implement caching for frequently accessed data
2. Add support for scheduled transfers
3. Enhance error reporting and monitoring
4. Implement transaction reconciliation
5. Add support for international transfers 