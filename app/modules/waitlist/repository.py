# app/modules/waitlist/repository.py

from sqlalchemy.orm import Session

from app.modules.waitlist.model import Waitlist


class WaitlistRepository:

    @staticmethod
    def create(
        db: Session,
        data: dict
    ):
        waitlist = Waitlist(**data)

        db.add(waitlist)
        db.commit()
        db.refresh(waitlist)

        return waitlist

    @staticmethod
    def get_all(db: Session):
        return db.query(Waitlist).all()

    @staticmethod
    def get_by_id(
        db: Session,
        waitlist_id: int
    ):
        return (
            db.query(Waitlist)
            .filter(Waitlist.id == waitlist_id)
            .first()
        )

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(Waitlist)
            .filter(Waitlist.email == email)
            .first()
        )