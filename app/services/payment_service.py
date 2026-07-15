import requests
from app.core.config import settings


class PaymentGatewayService:

    BASE_URL = "https://api.paystack.co"

    @classmethod
    def initialize_payment(
        cls,
        email: str,
        amount: float
    ):
        url = f"{cls.BASE_URL}/transaction/initialize"

        headers = {
            "Authorization":
                f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type":
                "application/json"
        }

        payload = {
            "email": email,
            "amount": int(amount * 100),  # <-- Added comma
            "callback_url": settings.PAYSTACK_CALLBACK_URL
        }

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=30  # <-- Added comma before timeout
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            return {
                "status": False,
                "message": str(e)
            }

    @classmethod
    def verify_payment(
        cls,
        reference: str
    ):
        url = (
            f"{cls.BASE_URL}/transaction/verify/"
            f"{reference}"
        )

        headers = {
            "Authorization":
                f"Bearer {settings.PAYSTACK_SECRET_KEY}"
        }

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            return {
                "status": False,
                "message": str(e)
            }