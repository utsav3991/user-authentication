from fastapi import APIRouter

from app import schema

router = APIRouter()

@router.post("/user/", response_model=schema.User)
def create_user(user: schema.UserCreate):
    return {'id':1, **user.dict()}
