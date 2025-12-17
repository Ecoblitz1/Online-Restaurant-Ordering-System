from pydantic import BaseModel, Field

class PaymentBase(BaseModel):
    order_id: int = Field(..., example=1)
    payment_type: str = Field(..., example="Credit Card")
    amount: float = Field(..., example=25.99)


class PaymentCreate(PaymentBase):
    pass


class PaymentOut(PaymentBase):
    id: int

    class Config:
        from_attributes = True
