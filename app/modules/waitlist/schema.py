from pydantic import BaseModel, EmailStr


class WaitlistCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None


class WaitlistResponse(BaseModel):
    id: int
    full_name: str
    email: str
    phone: str | None = None

    class Config:
        from_attributes = True