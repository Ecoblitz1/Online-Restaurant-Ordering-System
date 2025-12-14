from pydantic import BaseModel, Field
from datetime import date


class PromotionBase(BaseModel):
    code: str = Field(..., example="SAVE10")
    expiration_date: date = Field(..., example="2025-12-31")


class PromotionCreate(PromotionBase):
    pass


class PromotionOut(PromotionBase):
    id: int

    class Config:
        from_attributes = True
