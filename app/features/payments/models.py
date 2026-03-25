from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, func, String
from datetime import datetime
from app.core.database import Base

class Transaction(Base):
  __tablename__ = "transactions"

  id: Mapped[int] = mapped_column(primary_key=True)
  tenant_id: Mapped[int] = mapped_column(ForeignKey("tenants.id"))
  amount: Mapped[int] = mapped_column()
  category: Mapped[str] = mapped_column(String(20), default="rent")
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

  tenant: Mapped["Tenant"] = relationship("Tenant", back_populates="transactions")