# app/modules/auth/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user

from app.modules.auth.schema import (
    UserCreate,
    UserLogin,
)

from app.modules.auth.service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    user = AuthService.register(
        db=db,
        email=payload.email,
        full_name=payload.full_name,
        password=payload.password,
    )

    return {
        "message": "User created",
        "user_id": user.id,
    }


@router.post("/login")
def login(
    payload: UserLogin,
    db: Session = Depends(get_db),
):
    token = AuthService.login(
        db=db,
        email=payload.email,
        password=payload.password,
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return token


@router.get("/me")
def me(
    current_user=Depends(get_current_user),
):
    return current_user