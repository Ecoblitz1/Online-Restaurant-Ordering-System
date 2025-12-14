from ..dependencies.database import engine, Base

from .customers import Customer
from .menu_items import MenuItem
from .orders import Order
from .order_items import OrderItem
from .payments import Payment
from .reviews import Review
from .promotions import Promotion

def index():
    Base.metadata.create_all(bind=engine)
