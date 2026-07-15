from app.core.database import SessionLocal

from app.modules.notification.model import (
    Notification
)


def send_pending_notifications():

    db = SessionLocal()

    try:

        notifications = db.query(
            Notification
        ).filter(
            Notification.is_sent == False
        ).all()

        for notification in notifications:

            print(
                f"Sending Notification: {notification.id}"
            )

            notification.is_sent = True

        db.commit()

    finally:

        db.close()