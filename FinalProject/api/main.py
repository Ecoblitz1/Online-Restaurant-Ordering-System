import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from .routers import index as indexRoute
from api.routers import (
    customers,
    menu_items,
    orders,
    order_items,
    payments,
    reviews,
    promotions
)

# Models loader
from .models import model_loader
from .dependencies.config import conf

app = FastAPI(title="Online Restaurant Ordering System API")

# CORS settings
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models and create tables
model_loader.index()

# Include routers
app.include_router(customers.router)
app.include_router(menu_items.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.include_router(payments.router)
app.include_router(reviews.router)
app.include_router(promotions.router)

# Optional: load additional routes from indexRoute
indexRoute.load_routes(app)

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port, reload=True)
