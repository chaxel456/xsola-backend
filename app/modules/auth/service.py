# app/modules/auth/service.py

from fastapi import HTTPException, status
from sqlalchemy.orm import Session


from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.modules.auth.repository import AuthRepository


class AuthService:

    @staticmethod
    def register(
        db: Session,
        email: str,
        full_name: str,
        password: str,
    ):

        existing_user = AuthRepository.get_by_email(
            db,
            email
        )

        raise HTTPException(                  
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
             )

        return AuthRepository.create_user(
            db,
            {
                "email": email,
                "full_name": full_name,
                "password_hash": hash_password(password),
                "role": "staff",
            }
        )

    @staticmethod
    def login(
        db: Session,
        email: str,
        password: str,
    ):

        user = AuthRepository.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash
        ):
            return None

        token = create_access_token(
            str(user.id)
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }