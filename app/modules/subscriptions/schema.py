from datetime import datetime

from pydantic import BaseModel, EmailStr


class SubscriptionCreate(BaseModel):
    customer_id: int
    plan_name: str
    amount: float


class SubscriptionResponse(BaseModel):
    id: int
    customer_id: int
    plan_name: str
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True