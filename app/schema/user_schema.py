import uuid
from pydantic import BaseModel, EmailStr, field_validator


class UserListResponse(BaseModel):
    id: uuid.UUID
    email: str
    nickname: str
    is_active: bool

    model_config = {"from_attributes": True}

class UserDetailResponse(UserListResponse):
    password_hash: str
    is_active: bool

class UserCreateRequest(BaseModel):
    email: EmailStr
    password: str
    nickname: str

    @field_validator('password')
    def password_validator(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if len(v.encode("utf-8")) > 72:
            raise ValueError("Password must be at most 72 characters long")
        return v

    @field_validator('nickname')
    def nickname_validator(cls, v):
        if len(v) < 2 or len(v) > 8:
            raise ValueError("Nickname must be between 2 and 8 characters long")
        return v