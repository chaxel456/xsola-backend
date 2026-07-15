from pydantic import BaseModel
from datetime import datetime


class NotificationCreate(BaseModel):
    customer_id: int | None = None
    title: str
    message: str
    notification_type: str = "system"


class NotificationResponse(BaseModel):
    id: int
    customer_id: int | None
    title: str
    message: str
    notification_type: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True