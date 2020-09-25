from sqlalchemy.orm import Session

from app import security, models, schema


def create_user(db: Session, user: schema.UserCreate):
    hashed_password = security.hash_pw(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    try:
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()
    return db_user

