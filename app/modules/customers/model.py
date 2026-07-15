from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    phone = Column(String(20), unique=True, nullable=False)

    address = Column(String(255), nullable=True)

    status = Column(String(50), default="active")

    created_at = Column(DateTime(timezone=True), server_default=func.now())