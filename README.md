# Internet Banking Solution

A secure, scalable, and modular internet banking system integrated with Flexcube 14.3 Core Banking System.

## Features

- Secure user authentication with JWT and OTP
- Account management and balance inquiry
- Transaction history
- Internal funds transfer
- Role-based access control
- Integration with Core Banking System via SOAP XML

## Tech Stack

### Backend
- FastAPI (Python web framework)
- PostgreSQL (Database)
- Redis (Caching)
- Celery (Task Queue)

### Frontend
- Vue.js 3
- TailwindCSS
- Vuex (State Management)
- Vue Router

### Infrastructure
- Docker & Kubernetes
- GitHub Actions (CI/CD)
- Nginx (Web Server)
- Prometheus & Grafana (Monitoring)

## Getting Started

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

4. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Access the API documentation at `http://localhost:8000/docs`

## Project Structure

```
salaam-ib/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py
│   │   │   ├── accounts.py
│   │   │   └── transfers.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   ├── schemas/
│   └── services/
│       └── cbs/
├── tests/
├── docker/
└── frontend/
```

## Security Features

- JWT-based authentication
- OTP verification for sensitive operations
- Role-based access control
- Secure password hashing
- Rate limiting
- HTTPS enforcement

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

This project is proprietary and confidential. 