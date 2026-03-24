import secrets
from datetime import datetime, timezone, timedelta

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.exceptions import BadRequestException
from app.core.security import session_store
from app.core.security import verify_password, create_access_token, create_session, delete_session
from app.data.refreshtoken import RefreshToken
from app.schema.auth_schema import LoginRequest, TokenResponse, SessionInfo
from app.service.user_service import find_user_by_id, find_user_by_email


def login_jwt(db: Session, dto: LoginRequest) -> TokenResponse:
    user = find_user_by_email(db, dto.email)

    if not user or not verify_password(dto.password, user.password_hash):
        raise BadRequestException("Incorrect email or password")
    if not user.is_active:
        raise BadRequestException("Inactive user")

    db.execute(
        delete(RefreshToken)
        .where(RefreshToken.user_id == user.id)
    )

    raw_refresh_token = secrets.token_urlsafe(64)
    expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    db.add(RefreshToken(
        user_id=user.id,
        token=raw_refresh_token,
        expires_at=expires_at,
    ))

    return TokenResponse(
        access_token=create_access_token(str(user.id)),
        refresh_token=raw_refresh_token
    )

def refresh_token(db: Session, refresh_token_str: str) -> TokenResponse:
    result = db.execute(
        select(RefreshToken)
        .where(RefreshToken.token == refresh_token_str)
    )
    token = result.scalar_one_or_none()

    if not token:
        raise BadRequestException("Refresh token not found")
    if token.expires_at < datetime.now(timezone.utc):
        db.delete(token)
        raise BadRequestException("Refresh token expired")

    user = find_user_by_id(db, token.user_id)
    if not user or not user.is_active:
        raise BadRequestException("User not found or inactive")

    db.delete(token)

    new_refresh_token = secrets.token_urlsafe(64)
    expires_at = datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    db.add(RefreshToken(
        user_id=user.id,
        token=new_refresh_token,
        expires_at=expires_at,
    ))

    return TokenResponse(
        access_token=create_access_token(str(user.id)),
        refresh_token=new_refresh_token
    )

def logout_jwt(db: Session, refresh_token_str: str) -> None:
    db.execute(
        delete(RefreshToken)
        .where(RefreshToken.token == refresh_token_str)
    )


"""
Session Method
"""

def login_session(db: Session, dto: LoginRequest) -> str:
    user = find_user_by_email(db, dto.email)
    if not user or not verify_password(dto.password, user.password_hash):
        raise BadRequestException("Incorrect email or password")
    if not user.is_active:
        raise BadRequestException("Inactive user")

    session_id = create_session()
    session_store[session_id] = SessionInfo(user_id=user.id, email=user.email)
    print(session_id)
    return session_id

def logout_session(session_id: str) -> None:
    delete_session(session_id)