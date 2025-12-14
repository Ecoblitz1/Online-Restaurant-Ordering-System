from pydantic import BaseModel, Field
from typing import Optional

class MenuItemBase(BaseModel):
    name: str = Field(..., example="Veggie Burger")
    description: Optional[str] = Field(None, example="Grilled veggie patty with lettuce")
    price: float = Field(..., example=9.99)
    calories: Optional[int] = Field(None, example=450)
    category: Optional[str] = Field(None, example="Vegetarian")


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    category: Optional[str] = None


class MenuItemOut(MenuItemBase):
    id: int

    class Config:
        from_attributes = True
