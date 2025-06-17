from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True  # Para compatibilidade com SQLAlchemy (opcional)