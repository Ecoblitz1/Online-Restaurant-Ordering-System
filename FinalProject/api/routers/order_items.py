from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.order_items import OrderItemCreate, OrderItemOut
from ..models.order_items import OrderItem
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)

# CREATE order item
@router.post("/", response_model=OrderItemOut)
def create_order_item(item: OrderItemCreate, db: Session = Depends(get_db)):
    new_item = OrderItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

# READ all order items
@router.get("/", response_model=List[OrderItemOut])
def get_order_items(db: Session = Depends(get_db)):
    return db.query(OrderItem).all()

# READ single order item
@router.get("/{item_id}", response_model=OrderItemOut)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item

# DELETE order item
@router.delete("/{item_id}")
def delete_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    db.delete(item)
    db.commit()
    return {"message": "Order item deleted successfully"}
