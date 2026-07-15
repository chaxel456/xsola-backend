# app/modules/subscriptions/service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.subscriptions.repository import (
    SubscriptionRepository,
)


class SubscriptionService:

    @staticmethod
    def create_subscription(
        db: Session,
        customer_id: int,
        plan_name: str,
    ):

        return SubscriptionRepository.create(
            db,
            {
                "customer_id": customer_id,
                "plan_name": plan_name,
                "status": "active",
            }
        )

    @staticmethod
    def get_all_subscriptions(
        db: Session,
    ):
        return SubscriptionRepository.get_all(db)

    @staticmethod
    def get_subscription_by_id(
        db: Session,
        subscription_id: int,
    ):

        subscription = (
            SubscriptionRepository.get_by_id(
                db,
                subscription_id,
            )
        )

        if not subscription:
            raise HTTPException(
                status_code=404,
                detail="Subscription not found",
            )

        return subscription

    @staticmethod
    def get_customer_subscriptions(
        db: Session,
        customer_id: int,
    ):
        return (
            SubscriptionRepository.get_by_customer_id(
                db,
                customer_id,
            )
        )