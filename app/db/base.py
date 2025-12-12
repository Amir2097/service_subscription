from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings


# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass

