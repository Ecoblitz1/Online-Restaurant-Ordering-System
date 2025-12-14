from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..schemas.menu_items import MenuItemCreate, MenuItemUpdate, MenuItemOut
from ..models.menu_items import MenuItem
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/menu-items",
    tags=["Menu Items"]
)


# CREATE menu item
@router.post("/", response_model=MenuItemOut)
def create_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    new_item = MenuItem(**item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


# READ all menu items (optional filter by category)
@router.get("/", response_model=List[MenuItemOut])
def get_menu_items(category: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(MenuItem)
    if category:
        query = query.filter(MenuItem.category.ilike(f"%{category}%"))
    return query.all()


# READ single menu item
@router.get("/{item_id}", response_model=MenuItemOut)
def get_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item


# UPDATE menu item
@router.put("/{item_id}", response_model=MenuItemOut)
def update_menu_item(item_id: int, item_data: MenuItemUpdate, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    for key, value in item_data.dict(exclude_unset=True).items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


# DELETE menu item
@router.delete("/{item_id}")
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    db.delete(item)
    db.commit()
    return {"message": "Menu item deleted successfully"}
