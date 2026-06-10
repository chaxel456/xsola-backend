import uuid

from sqlalchemy import (
    Column,
    String,
    DateTime,
    Boolean
)

from sqlalchemy.sql import func

from app.core.database import Base


class Waitlist(Base):
    __tablename__ = "waitlist"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    full_name = Column(
        String,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    company_name = Column(
        String,
        nullable=True
    )

    phone = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="pending"
    )

    contacted = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )