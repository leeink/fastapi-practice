from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_size=10,
    max_overflow=10,
)

SyncSessionLocal = sessionmaker(
    engine,
    class_ = Session,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

def get_db() -> Session:
    with SyncSessionLocal() as session:
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise