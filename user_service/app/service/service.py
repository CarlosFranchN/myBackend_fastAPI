from app.database.models.users import User
from app.database.config import get_db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db):
    return db.query(User).all()