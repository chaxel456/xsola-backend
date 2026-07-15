# app/modules/subscriptions/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.subscriptions.schema import (
    SubscriptionCreate,
)

from app.modules.subscriptions.service import (
    SubscriptionService,
)

router = APIRouter()


@router.post("/")
def create_subscription(
    payload: SubscriptionCreate,
    db: Session = Depends(get_db),
):
    return SubscriptionService.create_subscription(
        db=db,
        customer_id=payload.customer_id,
        plan_name=payload.plan_name,
    )


@router.get("/")
def get_subscriptions(
    db: Session = Depends(get_db),
):
    return SubscriptionService.get_all_subscriptions(
        db
    )


@router.get("/{subscription_id}")
def get_subscription_by_id(
    subscription_id: int,
    db: Session = Depends(get_db),
):
    return SubscriptionService.get_subscription_by_id(
        db,
        subscription_id,
    )


@router.get("/customer/{customer_id}")
def get_customer_subscriptions(
    customer_id: int,
    db: Session = Depends(get_db),
):
    return SubscriptionService.get_customer_subscriptions(
        db,
        customer_id,
    )