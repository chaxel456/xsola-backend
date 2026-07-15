from fastapi import HTTPException

from app.modules.notification.repository import (
    NotificationRepository
)

from app.services.notification_service import (
    NotificationService
)


class NotificationsService:

    def __init__(self):
        self.repo = NotificationRepository()
        self.notification_service = NotificationService()

    def create_notification(
        self,
        db,
        payload
    ):
        notification = self.repo.create(
            db,
            payload.model_dump()
        )

        return notification

    def get_notifications(
        self,
        db
    ):
        return self.repo.get_all(db)

    def get_notification(
        self,
        db,
        notification_id
    ):
        notification = self.repo.get_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        return notification

    def mark_as_read(
        self,
        db,
        notification_id
    ):
        notification = self.repo.get_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        notification.is_read = True

        return self.repo.update(
            db,
            notification
        )

    def delete_notification(
        self,
        db,
        notification_id
    ):
        notification = self.repo.get_by_id(
            db,
            notification_id
        )

        if not notification:
            raise HTTPException(
                status_code=404,
                detail="Notification not found"
            )

        self.repo.delete(
            db,
            notification
        )

        return {
            "message": "Notification deleted"
        }

