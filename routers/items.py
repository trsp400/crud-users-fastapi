from fastapi import APIRouter
from schemas import ItemSchema

router = APIRouter()

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None, prodId: int = None):
    return {
        "item_id": item_id,
        "q": q,
        "prodId": prodId
    }

@router.put("/items/{item_id}")
def update_item(item_id: int, item: ItemSchema):
    return {
        "item_name": item.name,
        "item_id": item_id
    }
