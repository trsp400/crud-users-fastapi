from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from schemas import UserSchema
import crud

router = APIRouter()

@router.get("/", response_model=List[UserSchema])
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@router.post("/", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
  
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
  return crud.get_user(db, user_id=user_id)
