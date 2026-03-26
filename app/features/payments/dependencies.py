from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.features.payments.repository import PaymentRepository
from app.features.payments.service import PaymentService

async def get_payment_service(db: AsyncSession = Depends(get_db)) -> PaymentService:
    repo = PaymentRepository(db)
    return PaymentService(repo)