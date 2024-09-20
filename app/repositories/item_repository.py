from sqlalchemy.orm import Session
from app.models.item import Item

class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, item: Item):
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get(self, item_id: int):
        return self.db.query(Item).filter(Item.id == item_id).first()

    def get_all(self):
        return self.db.query(Item).all()