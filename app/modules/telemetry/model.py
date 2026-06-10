import uuid

from sqlalchemy import (
    Column,
    String,
    Float,
    DateTime,
    ForeignKey,
    JSON
)

from sqlalchemy.sql import func

from app.core.database import Base


class Telemetry(Base):
    __tablename__ = "telemetry"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    device_id = Column(
        String,
        ForeignKey("devices.id"),
        nullable=False
    )

    temperature = Column(Float, nullable=True)
    voltage = Column(Float, nullable=True)
    current = Column(Float, nullable=True)
    power = Column(Float, nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    raw_data = Column(JSON, nullable=True)

    timestamp = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )