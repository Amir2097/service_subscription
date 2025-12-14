from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass


# Создаем async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=False,  # SQL-логирование (полезно для дебага)
    future=True
)


# SessionLocal — фабрика сессий
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


# Dependency для FastAPI
async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
