# API 라우터
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.item import ItemCreate, ItemResponse
from services.item_service import create_item, get_item
from database import get_db

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse, status_code=201)
async def create_new_item(item: ItemCreate, db: Session = Depends(get_db)) -> ItemResponse:
    """새로운 아이템을 생성합니다."""
    return create_item(db, item)

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    """특정 아이템을 ID로 조회합니다."""
    return get_item(db, item_id)