import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Boolean
from src.database import ModelBase

class User(ModelBase):   
    __tablename__ = "users"

    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = Column(String(length=255))
    last_name = Column(String(length=255))
    status = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)