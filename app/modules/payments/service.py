import uuid

from fastapi import HTTPException

from app.modules.payments.repository import (
    PaymentRepository
)
from app.services.payment_service import PaymentGatewayService

class PaymentService:

    def __init__(self):
        self.repo = PaymentRepository()

    def create_payment(
        self,
        db,
        payload
    ):

        data = payload.model_dump()

        data["transaction_ref"] = (
            f"PAY-{uuid.uuid4().hex[:10]}"
        )

        data["status"] = "successful"

        return self.repo.create(
            db,
            data
        )

    def get_payments(
        self,
        db
    ):
        return self.repo.get_all(db)

    def get_payment(
        self,
        db,
        payment_id
    ):

        payment = self.repo.get_by_id(
            db,
            payment_id
        )

        if not payment:
            raise HTTPException(
                status_code=404,
                detail="Payment not found"
            )

        return payment
    ...

    def delete_payment(
        self,
        db,
        payment_id
    ):

        payment = self.repo.get_by_id(
            db,
            payment_id
        )

        if not payment:
            raise HTTPException(
                status_code=404,
                detail="Payment not found"
            )

        self.repo.delete(
            db,
            payment
        )

        return {
            "message": "Payment deleted"
        }

    # ---------------------------
    # ADD THESE BELOW
    # ---------------------------

    def initialize_payment(
        self,
        email: str,
        amount: float
    ):
        return PaymentGatewayService.initialize_payment(
            email=email,
            amount=amount
        )

    def verify_payment(
        self,
        db,
        reference: str
    ):
        response = PaymentGatewayService.verify_payment(
            reference
        )

        # Later we'll save/update the payment in the database here.

        return response

    def process_webhook(
        self,
        db,
        payload
    ):

        event = payload.get("event")

        if event != "charge.success":
            return {
                "message": "ignored"
            }

        data = payload.get("data")

        reference = data.get("reference")

        amount = data.get("amount") / 100

        email = data.get("customer", {}).get(
            "email"
        )

        print(
            f"Payment received: {reference}"
        )

        return {
            "status": "success",
            "reference": reference,
            "email": email,
            "amount": amount
        }