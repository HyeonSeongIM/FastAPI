# models/member.py
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)  # 비밀번호는 해시된 상태로 저장
    created_at = Column(DateTime, server_default=func.now())