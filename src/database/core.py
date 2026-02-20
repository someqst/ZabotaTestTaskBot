from data.config import settings

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine(url=settings.DB_URL)

LocalSession = async_sessionmaker(bind=engine)
