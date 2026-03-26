from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.config import settings

# Load models for SQLAlchemy registry
from app.domain.identity import User
from app.domain.properties import Room
from app.domain.members import Tenant
from app.features.payments.models import Transaction

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="3.0.0",
    openapi_url="/api/v1/openapi.json"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
  return {
    "status": "online",
    "engine": "Natakos V3"
  }


