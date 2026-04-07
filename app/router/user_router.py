import uuid

from fastapi import APIRouter, status, Request, Response
from starlette.responses import HTMLResponse, RedirectResponse

from schema.user_schema import UserListResponse, UserDetailResponse, UserCreateRequest
from core.config import templates

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/",
            response_class=HTMLResponse,
            status_code=status.HTTP_200_OK,
            summary="Get all users")
def get_users(request: Request):
    users = [
        UserListResponse(id = uuid.UUID("550e8400-e29b-41d4-a716-446655440000"),
                         email = "u1@wxample.com",
                         nickname="u1",
                         is_active = True,),
        UserListResponse(id=uuid.UUID("f47ac10b-58cc-4372-a567-0e02b2c3d479"),
                         email="u2@wxample.com",
                         nickname="u2",
                         is_active=True, ),
        UserListResponse(id=uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8"),
                         email="u3@wxample.com",
                         nickname="u3",
                         is_active=True, )
    ]
    return templates.TemplateResponse(
        request,
        "users.html",
        {
            "site_name": "Sync Base FastAPI's Users",
            "users": users,
        }
    )

@router.post("/login",
            response_class=RedirectResponse,
            status_code=status.HTTP_303_SEE_OTHER,
            summary="Login user")
def login(request: Request):
    return RedirectResponse(url="/user", status_code=status.HTTP_303_SEE_OTHER)

@router.post("/create",
             status_code=status.HTTP_201_CREATED,
             summary="Create a new user")
def create_user_route(dto: UserCreateRequest):
    return