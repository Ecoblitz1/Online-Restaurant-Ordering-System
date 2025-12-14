from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    calories = Column(Integer)
    category = Column(String(50))  # spicy, kids, vegetarian, etc.

    order_items = relationship("OrderItem", back_populates="menu_item")
