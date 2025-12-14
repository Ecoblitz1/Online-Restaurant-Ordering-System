from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class OrderBase(BaseModel):
    order_type: str = Field(..., example="delivery")  # pickup / delivery
    total_price: float = Field(..., example=24.99)


class OrderCreate(OrderBase):
    customer_id: int
    tracking_number: str = Field(..., example="ORD-123456")


class OrderUpdate(BaseModel):
    status: Optional[str] = Field(None, example="preparing")


class OrderOut(OrderBase):
    id: int
    tracking_number: str
    status: str
    created_at: datetime
    customer_id: int

    class Config:
        from_attributes = True
