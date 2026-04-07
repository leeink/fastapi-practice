from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.router import user_router
from core.config import templates

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Sync Base FastAPI",
    version="0.0.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

app.include_router(user_router.router)
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {"site_name": "Sync Base FastAPI"}
    )

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/.well-known/appspecific/com.chrome.devtools.json")
def chrome_devtools():
    return {}
