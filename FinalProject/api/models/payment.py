from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    payment_type = Column(String(50))  # card, cash, etc.
    transaction_status = Column(String(50))
    amount = Column(Float)

    order_id = Column(Integer, ForeignKey("orders.id"))

    order = relationship("Order", back_populates="payment")
