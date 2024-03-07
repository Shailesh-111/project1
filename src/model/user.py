import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Boolean
from src.database import Base

class User(Base):   
    __tablename__ = "users"

    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    status = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)