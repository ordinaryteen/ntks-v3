from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.core.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), index=True)
    phone_number: Mapped[str] = mapped_column(String(20), unique=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), nullable=True)

    room: Mapped["Room"] = relationship("Room", back_populates="tenants")
    transactions: Mapped[list["Transaction"]] = relationship("Transaction", back_populates="tenant")