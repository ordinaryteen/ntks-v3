from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.domain.properties import Room
from app.domain.members import Tenant
from app.features.payments.models import Transaction

class PaymentRepository:
  def __init__(self, session: AsyncSession):
    self.session = session

  async def get_room_by_name(self, room_name: str):
    stmt = select(Room).where(func.upper(Room.room_name) == room_name.upper())
    result = await self.session.execute(stmt)
    
    return result.scalar_one_or_none()

  async def get_tenant_by_name_and_room(self, name: str, room_id: int):
    stmt = select(Tenant).where(
      func.lower(Tenant.name).contains(name.lower()),
      Tenant.room_id == room_id
    )
    result = await self.session.execute(stmt)

    return result.scalar_one_or_none()

  async def create_transaction(self, tenant_id: int, amount: int, category: str = "rent"):
    new_tx = Transaction(
      tenant_id = tenant_id,
      amount = amount,
      category = category
    )

    self.session.add(new_tx)
    await self.session.flush()
    return new_tx