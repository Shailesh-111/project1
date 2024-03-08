import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base, as_declarative
from sqlalchemy.orm import sessionmaker
from src.config import config

load_dotenv()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
# engine = create_async_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()

async def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@as_declarative()
class ModelBase:
    __name__: str
    __tablename__:  str