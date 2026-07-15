from sqlalchemy.orm import Session

from app.modules.notification.model import Notification


class NotificationRepository:

    def create(
        self,
        db: Session,
        data: dict
    ):
        notification = Notification(**data)

        db.add(notification)
        db.commit()
        db.refresh(notification)

        return notification

    def get_all(
        self,
        db: Session
    ):
        return db.query(Notification).all()

    def get_by_id(
        self,
        db: Session,
        notification_id: int
    ):
        return (
            db.query(Notification)
            .filter(
                Notification.id == notification_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        notification
    ):
        db.commit()
        db.refresh(notification)

        return notification

    def delete(
        self,
        db: Session,
        notification
    ):
        db.delete(notification)
        db.commit()

def get_all(
        self,
        db: Session
    ):
        return db.query(
            Notification
        ).all()

def get_by_id(
        self,
        db: Session,
        notification_id: int
    ):
        return db.query(
            Notification
        ).filter(
            Notification.id == notification_id
        ).first()