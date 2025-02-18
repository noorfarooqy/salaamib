from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from app.core.config import settings
from app.api.v1 import auth, accounts, transfers

app = FastAPI(
    title=settings.APP_NAME,
    description="Internet Banking Solution API",
    version="1.0.0",
    # Configure OAuth2 for Swagger UI
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True,
        "clientId": "swagger",
    }
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix=settings.API_V1_PREFIX + "/auth", tags=["Authentication"])
app.include_router(accounts.router, prefix=settings.API_V1_PREFIX + "/accounts", tags=["Accounts"])
app.include_router(transfers.router, prefix=settings.API_V1_PREFIX + "/transfers", tags=["Transfers"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Salaam Internet Banking API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    } 