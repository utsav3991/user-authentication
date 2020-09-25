from pydantic import BaseSettings

from app.env import DB_URL


class Settings(BaseSettings):
    secret_key: str = "123!@#^&"
    sqlalchemy_url: str = DB_URL

settings = Settings()