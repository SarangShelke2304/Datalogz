from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

engine = create_async_engine(DATABASE_URL)
local_session = sessionmaker(bind=engine, class_= AsyncSession, expire_on_commit=False)

async def get_db():
    async with local_session() as session:
        yield session
