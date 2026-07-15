from pydantic import BaseModel, EmailStr



class PaymentCreate(BaseModel):
    customer_id: int
    amount: float
    payment_method: str


class PaymentResponse(BaseModel):
    id: int
    customer_id: int
    amount: float
    payment_method: str
    transaction_ref: str
    status: str

    class Config:
        from_attributes = True

class InitializePaymentRequest(BaseModel):
    email: EmailStr
    amount: float