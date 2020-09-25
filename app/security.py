from datetime import datetime, timedelta

from passlib.context import CryptContext
import jwt

from app.settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_pw(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str):
    expire = datetime.now() + timedelta(minutes=30)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm='HS256')
    return encoded_jwt
