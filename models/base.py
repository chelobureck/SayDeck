from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config.settings import get_settings
import ssl

settings = get_settings()
ssl_context = ssl.create_default_context()
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={"ssl": ssl_context}
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session 