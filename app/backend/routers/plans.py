from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models, schemas

router = APIRouter()

@router.get("/plans/", response_model=List[schemas.Plan])
def list_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    plans = db.query(models.Plan).offset(skip).limit(limit).all()
    return plans 