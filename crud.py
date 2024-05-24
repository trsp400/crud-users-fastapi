from sqlalchemy.orm import Session
from models import UserModel
from schemas import UserSchema

def get_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user: UserSchema):
    db_user = UserModel(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(UserModel).get(user_id)
    