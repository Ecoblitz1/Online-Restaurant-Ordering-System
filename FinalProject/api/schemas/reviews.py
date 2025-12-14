from pydantic import BaseModel, Field
from typing import Optional


class ReviewBase(BaseModel):
    rating: int = Field(..., example=5)
    comment: Optional[str] = Field(None, example="Food was excellent!")


class ReviewCreate(ReviewBase):
    customer_id: int


class ReviewOut(ReviewBase):
    id: int
    customer_id: int

    class Config:
        from_attributes = True
