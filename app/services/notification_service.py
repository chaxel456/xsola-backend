from app.services.email_service import EmailService
from app.services.sms_service import SMSService


class NotificationService:

    def __init__(self):

        self.email = EmailService()
        self.sms = SMSService()

    def send_email_notification(
        self,
        recipient,
        subject,
        message
    ):

        return self.email.send_email(
            recipient,
            subject,
            message
        )

    def send_sms_notification(
        self,
        phone,
        message
    ):

        return self.sms.send_sms(
            phone,
            message
        )