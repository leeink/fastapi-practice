import uuid
from typing import Any

from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictException
from app.core.security import hash_password
from app.data.user import User
from app.schema.user_schema import UserCreateRequest


def find_user_all(db: Session) -> Sequence[Any]:
    result = db.execute(
        select(User)
    )
    return result.scalars().all()

def find_user_by_id(db: Session, user_id: str | uuid.UUID) -> User | None:
    result = db.execute(
        select(User)
        .where(User.id == user_id)
    )

    return result.scalar_one_or_none()

def find_user_by_email(db: Session, email: str) -> User | None:
    result = db.execute(
        select(User)
        .where(User.email == email)
    )
    return result.scalar_one_or_none()

def create_user(db: Session, dto: UserCreateRequest) -> User:
    if find_user_by_email(db, dto.email):
        raise ConflictException("Email already exists")

    user = User(
        email=dto.email,
        password_hash=hash_password(dto.password),
        nickname=dto.nickname
    )

    db.add(user)
    db.flush()

    return user