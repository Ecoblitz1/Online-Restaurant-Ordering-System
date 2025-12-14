from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CustomerBase(BaseModel):
    name: str = Field(..., example="Jane Doe")
    email: Optional[EmailStr] = Field(None, example="jane@example.com")
    phone: str = Field(..., example="123-456-7890")
    address: Optional[str] = Field(None, example="123 Main St, City, State")


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class CustomerOut(CustomerBase):
    id: int

    class Config:
        from_attributes = True
