from pydantic import BaseModel, Field


class PaymentBase(BaseModel):
    payment_type str = Field(..., example="Credit Card") # credit_card, debit_card, cash etc.
    transaction_status: str = Field(..., example="Success")
    amount: float = Field(..., example=67.69)


  class PaymentCreate(PaymentBase):
    order_id: int


class PaymentOut(PaymentBase):
    id: int
    order_id: int

    class Config:
        from_attributes = True