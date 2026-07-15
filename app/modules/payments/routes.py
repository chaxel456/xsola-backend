from fastapi import (
    APIRouter,
    Depends,
    Request
)

print("PAYMENTS ROUTES LOADED")

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.payments.schema import (
    PaymentCreate,
    PaymentResponse
)

from app.modules.payments.service import (
    PaymentService
)

from app.services.payment_service import (
    PaymentGatewayService
)

from app.modules.payments.schema import (
    InitializePaymentRequest
)


router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

service = PaymentService()


@router.post(
    "/",
    response_model=PaymentResponse
)
def create_payment(
    payload: PaymentCreate,
    db: Session = Depends(get_db)
):

    return service.create_payment(
        db,
        payload
    )


@router.get(
    "/",
    response_model=list[PaymentResponse]
)
def get_payments(
    db: Session = Depends(get_db)
):

    return service.get_payments(db)


@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def get_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):

    return service.get_payment(
        db,
        payment_id
    )


@router.delete("/{payment_id}")
def delete_payment(
    payment_id: int,
    db: Session = Depends(get_db)
):

    return service.delete_payment(
        db,
        payment_id
    )

@router.post("/initialize")
def initialize_payment(
    payload: InitializePaymentRequest
):
    return PaymentGatewayService.initialize_payment(
        email=payload.email,
        amount=payload.amount
    )

@router.get("/verify/{reference}")
def verify_payment(
    reference: str
):
    return PaymentGatewayService.verify_payment(
        reference
    )

@router.post("/webhook")
async def paystack_webhook(
    request: Request,
    db: Session = Depends(get_db)
):
    payload = await request.json()

    return service.process_webhook(
        db,
        payload
    )