from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schema, dependency, checkers, crud

router = APIRouter()

@router.post("/user/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session= Depends(dependency.get_db)):
    db_user = checkers.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)
