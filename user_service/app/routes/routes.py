from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate,UserResponse
from user_service.app.database.models.models import create_user, get_all_users
from user_service.app.database.db_config import get_db


router = APIRouter()

@router.post("/users/", response_model=UserResponse, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, username=user.username, password=user.password)
    return db_user


@router.get("/users/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return get_all_users(db=db)


@router.get("/tables/")
def list_tables():
    tables = get_all_users()
    return {"tables": tables}