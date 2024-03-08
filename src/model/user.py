import uuid
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, String
from src.database import db

class User(db.Model):
    __tablename__ = "users"

    id = Column(String(36), default=lambda: str(uuid.uuid4()), primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(225))
    status = Column(Boolean)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
