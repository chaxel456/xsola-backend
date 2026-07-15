
# app/modules/users/service.py

from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.modules.users.model import User
from app.modules.users.schema import UserCreate, UserUpdate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:

    # --------------------------
    # HASH PASSWORD
    # --------------------------
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    # --------------------------
    # VERIFY PASSWORD
    # --------------------------
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    # --------------------------
    # CREATE USER
    # --------------------------
    def create_user(self, db: Session, user: UserCreate):
        hashed_password = self.hash_password(user.password)

        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password,
            full_name=user.full_name,
            phone=user.phone,
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    # --------------------------
    # GET USER BY ID
    # --------------------------
    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    # --------------------------
    # GET USER BY EMAIL
    # --------------------------
    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    # --------------------------
    # GET USER BY USERNAME
    # --------------------------
    def get_user_by_username(self, db: Session, username: str):
        return db.query(User).filter(User.username == username).first()

    # --------------------------
    # UPDATE USER
    # --------------------------
    def update_user(self, db: Session, user_id: int, data: UserUpdate):
        user = self.get_user(db, user_id)

        if not user:
            return None

        update_data = data.dict(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = self.hash_password(update_data["password"])
            del update_data["password"]

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user

    # --------------------------
    # DELETE USER
    # --------------------------
    def delete_user(self, db: Session, user_id: int):
        user = self.get_user(db, user_id)

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user