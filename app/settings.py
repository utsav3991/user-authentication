from pydantic import BaseSettings

from app.env import *


class Settings(BaseSettings):
    secret_key: str = SECRET
    sqlalchemy_url: str = DB_URL

settings = Settings()