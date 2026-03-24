import uuid

from pydantic import BaseModel
from datetime import datetime

class LoginRequest(BaseModel):
    email: str
    password: str

"""
JWT Schemas
"""
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshRequest(BaseModel):
    refresh_token: str

class LogoutJWTRequest(BaseModel):
    refresh_token: str


"""
Session Schemas
"""

class SessionInfo(BaseModel):
    user_id: uuid.UUID
    email: str
    created_at: datetime = datetime.now()

class LogoutSessionRequest(BaseModel):
    session_id: str