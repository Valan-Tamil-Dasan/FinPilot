from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.settings import get_settings

settings = get_settings()

SYNC_DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
    f"?sslmode=require"
)

engine = create_engine(SYNC_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)
