import uuid

from fastapi import APIRouter, status
from fastapi.params import Depends

from sqlalchemy.orm import Session
from app.data.user import User
from app.core.database import get_db
from app.core.exceptions import NotFoundException
from app.core.security import get_current_user
from app.schema.user_schema import UserListResponse, UserDetailResponse, UserCreateRequest
from app.service.user_service import find_user_all, find_user_by_id, create_user

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/",
            response_model=list[UserListResponse],
            summary="Get all users")
def get_users(db: Session = Depends(get_db)):
    return find_user_all(db)

@router.get("/me",
            response_model=UserListResponse,
            summary="Get current user")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}",
            response_model=UserDetailResponse,
            summary="Get user by id")
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = find_user_by_id(db, user_id)
    if not user:
        raise NotFoundException("User not found")
    return user

@router.post("/create",
             status_code=status.HTTP_201_CREATED,
             summary="Create a new user")
def create_user_route(dto: UserCreateRequest, db: Session = Depends(get_db)):
    create_user(db, dto)
