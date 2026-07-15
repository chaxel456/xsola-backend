class SMSService:

    def send_sms(
        self,
        phone: str,
        message: str
    ):

        print(
            f"SMS SENT TO {phone}"
        )

        print(message)

        return True