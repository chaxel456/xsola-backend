from pydantic import BaseModel


class PaymentCreate(BaseModel):
    customer_id: str
    amount: float
    provider: str


class PaymentResponse(BaseModel):
    id: str
    amount: float
    provider: str
    status: str

    class Config:
        from_attributes = True