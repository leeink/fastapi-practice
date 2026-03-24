import uuid

from fastapi import APIRouter, status, Request, Response
from fastapi.params import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schema.auth_schema import LoginRequest, TokenResponse, RefreshRequest, LogoutJWTRequest, LogoutSessionRequest
from app.schema.user_schema import UserListResponse, UserDetailResponse, UserCreateRequest
from app.service.auth_service import login_jwt, refresh_token, logout_jwt, login_session, logout_session
from app.service.user_service import find_user_all, find_user_by_id, create_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register",
             response_model=UserListResponse,
             status_code=status.HTTP_201_CREATED,
             summary="Register a new user")
def register_route(dto: UserCreateRequest, db: Session = Depends(get_db)):
    create_user(db, dto)


@router.post("/login",
             response_model=TokenResponse,
             status_code=status.HTTP_200_OK,
             summary="Login")
def login_jwt_route(dto: LoginRequest, db: Session = Depends(get_db)):
    return login_jwt(db, dto)


@router.post("/refresh",
             response_model=TokenResponse,
             summary="Refresh token")
def refresh_route(dto: RefreshRequest, db: Session = Depends(get_db)):
    return refresh_token(db, dto.refresh_token)


@router.post("/logout",
             status_code=status.HTTP_204_NO_CONTENT,
             summary="Logout")
def logout_jwt_route(dto: LogoutJWTRequest, db: Session = Depends(get_db)):
    return logout_jwt(db, dto.refresh_token)


@router.post("/login-session",
             status_code=status.HTTP_200_OK,
             summary="Login with session")
def login_session_route(dto: LoginRequest,
                        response: Response,
                        db: Session = Depends(get_db)):
    session_id = login_session(db, dto)

    response.set_cookie(
        "session_id",
        session_id,
        httponly=True,
        samesite="lax",
        max_age=3600,
        # secure=True,  # HTTPS 환경에서 활성화
    )
    return {"message": "로그인 성공"}


@router.post("/logout-session",
             status_code=status.HTTP_204_NO_CONTENT,
             summary="Logout with session")
def logout_session_route(request: Request, response: Response):
    logout_session(request.cookies.get("session_id"))
    response.delete_cookie("session_id")
    return {"message": "Logout"}
