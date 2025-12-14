from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..schemas.promotions import PromotionCreate, PromotionOut
from ..models.promotions import Promotion
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/promotions",
    tags=["Promotions"]
)

# CREATE promotion
@router.post("/", response_model=PromotionOut)
def create_promotion(promo: PromotionCreate, db: Session = Depends(get_db)):
    new_promo = Promotion(**promo.dict())
    db.add(new_promo)
    db.commit()
    db.refresh(new_promo)
    return new_promo

# READ all promotions
@router.get("/", response_model=List[PromotionOut])
def get_promotions(db: Session = Depends(get_db)):
    return db.query(Promotion).all()

# READ single promotion
@router.get("/{promo_id}", response_model=PromotionOut)
def get_promotion(promo_id: int, db: Session = Depends(get_db)):
    promo = db.query(Promotion).filter(Promotion.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo

# DELETE promotion
@router.delete("/{promo_id}")
def delete_promotion(promo_id: int, db: Session = Depends(get_db)):
    promo = db.query(Promotion).filter(Promotion.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(promo)
    db.commit()
    return {"message": "Promotion deleted successfully"}
