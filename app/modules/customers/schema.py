from pydantic import BaseModel, EmailStr
from datetime import datetime


class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    address: str | None = None


class CustomerUpdate(BaseModel):
    full_name: str | None = None
    phone: str | None = None
    address: str | None = None
    status: str | None = None


class CustomerResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str
    address: str | None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True