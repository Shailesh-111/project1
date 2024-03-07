from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    status: Optional[bool] = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class UsersCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass
