from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.sql import func

from app.core.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    device_id = Column(
        Integer,
        ForeignKey("devices.id"),
        nullable=False
    )

    voltage = Column(
        Float,
        nullable=False
    )

    current = Column(
        Float,
        nullable=False
    )

    power = Column(
        Float,
        nullable=False
    )

    battery = Column(
        Float,
        nullable=False
    )

    temperature = Column(
        Float,
        nullable=True
    )

    status = Column(
        String,
        default="online"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )