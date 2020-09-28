# from fastapi_mail import ConnectionConfig
from pydantic import BaseSettings

from app.env import *


class Settings(BaseSettings):
    secret_key: str = SECRET
    sqlalchemy_url: str = DB_URL

    # conf = ConnectionConfig(
    #     MAIL_USERNAME="94a75380ae919f",
    #     MAIL_PASSWORD="a01f9d7086441a",
    #     MAIL_PORT=2525,
    #     MAIL_SERVER="smtp.mailtrap.io",
    #     MAIL_TLS=True,
    #     MAIL_SSL=False
    # )

settings = Settings()