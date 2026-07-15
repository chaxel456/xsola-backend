# app/modules/waitlist/service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.waitlist.repository import WaitlistRepository


class WaitlistService:

    @staticmethod
    def create_waitlist(
        db: Session,
        full_name: str,
        email: str,
        phone: str | None = None,
    ):

        existing = WaitlistRepository.get_by_email(
            db,
            email
        )

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already on waitlist"
            )

        return WaitlistRepository.create(
            db,
            {
                "full_name": full_name,
                "email": email,
                "phone": phone,
            }
        )

    @staticmethod
    def get_all_waitlist(
        db: Session,
    ):
        return WaitlistRepository.get_all(db)

    @staticmethod
    def get_waitlist_by_id(
        db: Session,
        waitlist_id: int,
    ):

        waitlist = WaitlistRepository.get_by_id(
            db,
            waitlist_id
        )

        if not waitlist:
            raise HTTPException(
                status_code=404,
                detail="Waitlist entry not found"
            )

        return waitlist