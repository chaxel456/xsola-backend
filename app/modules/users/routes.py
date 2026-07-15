# app/modules/users/routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.users.service import UserService


router = APIRouter()


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    return UserService.get_all_users(db)


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(
        db,
        user_id
    )