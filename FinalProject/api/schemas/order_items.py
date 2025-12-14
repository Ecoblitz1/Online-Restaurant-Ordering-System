from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    menu_item_id: int = Field(..., example=1)
    quantity: int = Field(..., example=2)


class OrderItemCreate(OrderItemBase):
    order_id: int


class OrderItemOut(OrderItemBase):
    id: int
    order_id: int

    class Config:
        from_attributes = True
