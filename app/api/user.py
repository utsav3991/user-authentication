from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schema, dependency, validators
from app.crud import user_crud

router = APIRouter()

@router.post("/user/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session= Depends(dependency.get_db)):
    db_user = validators.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)
