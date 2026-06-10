from pydantic import BaseModel, EmailStr
from datetime import datetime


class WaitlistCreate(BaseModel):
    full_name: str
    email: EmailStr
    company_name: str | None = None
    phone: str | None = None


class WaitlistResponse(BaseModel):
    id: str
    full_name: str
    email: str
    company_name: str | None = None
    phone: str | None = None
    status: str
    contacted: bool
    created_at: datetime

    class Config:
        from_attributes = True