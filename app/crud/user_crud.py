from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from app import security, schema
from app.models import user_model
from app.tasks import send_email_task


async def create_user(db: Session, user: schema.UserCreate):
    hashed_password = security.hash_pw(user.password)
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.refresh(db_user)
        db.close()
    BackgroundTasks.add_task(send_email_task, 'abc@gmail.com', 'def@gmail.com', 'Welcome')
    return db_user
