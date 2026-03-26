from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from app.core.database import Base

class User(Base):
  __tablename__ = "users"

  id: Mapped[int] = mapped_column(primary_key=True)
  phone_number: Mapped[str] = mapped_column(String(20), unique=True, index=True)
  name: Mapped[str] = mapped_column(String(100), nullable=True)

  rooms: Mapped[list["Room"]] = relationship("Room", back_populates="owner")