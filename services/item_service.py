# 비지니스 로직
from sqlalchemy.orm import Session
from models.item import Item
from schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate) -> Item:
    db_item = Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise ValueError(f"Item with ID {item_id} not found")
    return item