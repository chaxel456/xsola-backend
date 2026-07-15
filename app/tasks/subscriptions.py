from datetime import datetime

from app.core.database import SessionLocal

from app.modules.subscriptions.model import (
    Subscription
)


def expire_subscriptions():

    db = SessionLocal()

    try:

        subscriptions = db.query(
            Subscription
        ).filter(
            Subscription.status == "active"
        ).all()

        for subscription in subscriptions:

            if subscription.end_date <= datetime.utcnow():

                subscription.status = "expired"

                print(
                    f"Expired Subscription: {subscription.id}"
                )

        db.commit()

    finally:

        db.close()