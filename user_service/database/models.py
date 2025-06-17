# models.py
from sqlalchemy import Column, Integer, String
# from database.db_config import Base
from db_config import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserModel(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)


# Funções de negócio
def create_user(db, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = UserModel(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_all_users(db):
    return db.query(UserModel).all()


def get_user_by_username(db, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()