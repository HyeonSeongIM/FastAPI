# routers/member.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.member import MemberCreate, MemberInDB, MemberUpdate
from services.member import create_member, get_member, get_members, update_member, delete_member
from database import get_db

router = APIRouter(prefix="/members", tags=["members"])

@router.post("/", response_model=MemberInDB)
def create_new_member(member: MemberCreate, db: Session = Depends(get_db)):
    return create_member(db, member)

@router.get("/{member_id}", response_model=MemberInDB)
def read_member(member_id: int, db: Session = Depends(get_db)):
    return get_member(db, member_id)

@router.get("/", response_model=List[MemberInDB])
def read_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_members(db, skip, limit)

@router.put("/{member_id}", response_model=MemberInDB)
def update_existing_member(member_id: int, member: MemberUpdate, db: Session = Depends(get_db)):
    return update_member(db, member_id, member)

@router.delete("/{member_id}")
def delete_existing_member(member_id: int, db: Session = Depends(get_db)):
    return delete_member(db, member_id)