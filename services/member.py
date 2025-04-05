# services/member.py
from sqlalchemy.orm import Session
from models.member import Member
from schemas.member import MemberCreate, MemberUpdate
from passlib.context import CryptContext
from fastapi import HTTPException

# 비밀번호 해싱 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# 멤버 생성
def create_member(db: Session, member: MemberCreate):
    # 이메일 중복 체크
    if db.query(Member).filter(Member.email == member.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = hash_password(member.password)
    db_member = Member(
        email=member.email,
        username=member.username,
        password=hashed_password
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

# 멤버 조회 (ID로)
def get_member(db: Session, member_id: int):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

# 모든 멤버 조회
def get_members(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Member).offset(skip).limit(limit).all()

# 멤버 업데이트
def update_member(db: Session, member_id: int, member_update: MemberUpdate):
    db_member = get_member(db, member_id)
    update_data = member_update.dict(exclude_unset=True)
    
    if "password" in update_data:
        update_data["password"] = hash_password(update_data["password"])
    
    for key, value in update_data.items():
        setattr(db_member, key, value)
    
    db.commit()
    db.refresh(db_member)
    return db_member

# 멤버 삭제
def delete_member(db: Session, member_id: int):
    db_member = get_member(db, member_id)
    db.delete(db_member)
    db.commit()
    return {"message": "Member deleted successfully"}