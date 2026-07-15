from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(
        Integer,
        ForeignKey("customers.id"),
        nullable=False
    )

    serial_number = Column(
        String(100),
        unique=True,
        nullable=False
    )

    device_type = Column(String(100))

    status = Column(
        String(50),
        default="active"
    )

    status = Column(
    String,
    default="inactive"
)

    installation_date = Column(DateTime(timezone=True))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    customer = relationship("Customer")