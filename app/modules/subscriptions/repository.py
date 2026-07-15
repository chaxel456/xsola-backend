# app/modules/subscriptions/repository.py

from sqlalchemy.orm import Session

from app.modules.subscriptions.model import Subscription


class SubscriptionRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict
    ):
        subscription = Subscription(**data)

        db.add(subscription)
        db.commit()
        db.refresh(subscription)

        return subscription

    @staticmethod
    def get_all(
        db: Session
    ):
        return db.query(Subscription).all()

    @staticmethod
    def get_by_id(
        db: Session,
        subscription_id: int
    ):
        return (
            db.query(Subscription)
            .filter(
                Subscription.id == subscription_id
            )
            .first()
        )

    @staticmethod
    def get_by_customer_id(
        db: Session,
        customer_id: int
    ):
        return (
            db.query(Subscription)
            .filter(
                Subscription.customer_id == customer_id
            )
            .all()
        )