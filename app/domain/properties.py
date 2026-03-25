from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from app.core.database import Base

class Room(Base):
  __tablename__ = "rooms"

  id: Mapped[int] = mapped_column(primary_key=True)
  room_name: Mapped[str] = mapped_column(String(10), unique=True, index=True)
  price: Mapped[int] = mapped_column(default=0)
  owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

  owner: Mapped["User"] = relationship("User", back_populates="rooms")
  tenants: Mapped[list["Tenant"]] = relationship("Tenant", back_populates="room")
