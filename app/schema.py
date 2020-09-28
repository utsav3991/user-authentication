from typing import List

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    is_active: bool


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class EmailSchema(BaseModel):
    email: List[EmailStr]
