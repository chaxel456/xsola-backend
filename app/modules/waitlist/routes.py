# app/modules/waitlist/routes.py


print("WAITLIST ROUTES LOADED")

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.modules.waitlist.schema import (
    WaitlistCreate,
)
from app.modules.waitlist.service import (
    WaitlistService,
)


router = APIRouter()


@router.post("/")
def create_waitlist(
    payload: WaitlistCreate,
    db: Session = Depends(get_db),
):
    return WaitlistService.create_waitlist(
        db=db,
        full_name=payload.full_name,
        email=payload.email,
        phone=payload.phone,
    )


@router.get("/")
def get_waitlist(
    db: Session = Depends(get_db),
):
    return WaitlistService.get_all_waitlist(
        db
    )


@router.get("/{waitlist_id}")
def get_waitlist_by_id(
    waitlist_id: int,
    db: Session = Depends(get_db),
):
    return WaitlistService.get_waitlist_by_id(
        db,
        waitlist_id,
    )


