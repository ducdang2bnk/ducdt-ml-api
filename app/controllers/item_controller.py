from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService

router = APIRouter()

@router.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return service.create_item(name, description)

@router.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return service.get_item(item_id)

@router.get("/items/")
def read_items(db: Session = Depends(get_db)):
    repository = ItemRepository(db)
    service = ItemService(repository)
    return service.get_all_items()