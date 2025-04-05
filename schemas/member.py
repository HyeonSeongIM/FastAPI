# schemas/member.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class MemberBase(BaseModel):
    email: EmailStr
    username: str

class MemberCreate(MemberBase):
    password: str

class MemberUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

class MemberInDB(MemberBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # orm_mode를 from_attributes로 변경