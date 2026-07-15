from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.notification.schema import (
    NotificationCreate,
    NotificationResponse
)

from app.modules.notification.service import (
    NotificationsService
)

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

service = NotificationsService()


@router.post(
    "/",
    response_model=NotificationResponse
)
def create_notification(
    payload: NotificationCreate,
    db: Session = Depends(get_db)
):
    return service.create_notification(
        db,
        payload
    )


@router.get(
    "/",
    response_model=list[NotificationResponse]
)
def get_notifications(
    db: Session = Depends(get_db)
):
    return service.get_notifications(db)


@router.get(
    "/{notification_id}",
    response_model=NotificationResponse
)
def get_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    return service.get_notification(
        db,
        notification_id
    )


@router.put(
    "/{notification_id}/read"
)
def mark_as_read(
    notification_id: int,
    db: Session = Depends(get_db)
):
    return service.mark_as_read(
        db,
        notification_id
    )


@router.delete(
    "/{notification_id}"
)
def delete_notification(
    notification_id: int,
    db: Session = Depends(get_db)
):
    return service.delete_notification(
        db,
        notification_id
    )