# app/modules/auth/repository.py

from sqlalchemy.orm import Session

from app.modules.auth.model import User


class AuthRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ) -> User | None:
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        user_id: int
    ) -> User | None:
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        user_data: dict
    ) -> User:

        user = User(**user_data)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user