# pydamic 스키마
from pydantic import BaseModel, Field

class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int

    class Config:
        orm_mode = True  # SQLAlchemy 객체를 자동으로 변환