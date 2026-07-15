import smtplib
from email.mime.text import MIMEText
from app.core.config import settings
from fastapi_mail import (
    FastMail,
    MessageSchema,
    ConnectionConfig
)


from app.core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USERNAME,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.SMTP_FROM,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_FROM_NAME=settings.SMTP_FROM_NAME,
    MAIL_STARTTLS=settings.SMTP_STARTTLS,
    MAIL_SSL_TLS=settings.SMTP_SSL_TLS,
    USE_CREDENTIALS=True
)

class EmailService:

    def send_email(
        self,
        recipient: str,
        subject: str,
        body: str
    ):

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = settings.EMAIL_FROM
        msg["To"] = recipient

        try:
            server = smtplib.SMTP(
                settings.SMTP_HOST,
                settings.SMTP_PORT
            )

            server.starttls()

            server.login(
                settings.SMTP_USERNAME,
                settings.SMTP_PASSWORD
            )

            server.send_message(msg)
            server.quit()

            return True

        except Exception as e:
            print(e)
            return False
        

    @staticmethod
    async def send_email(
        email: str,
        subject: str,
        body: str
    ):

        message = MessageSchema(
            subject=subject,
            recipients=[email],
            body=body,
            subtype="html"
        )

        fm = FastMail(conf)

        await fm.send_message(
            message
        )