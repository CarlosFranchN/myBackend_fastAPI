# main.py
from fastapi import FastAPI, HTTPException
from models.user import create_user, get_all_users

app = FastAPI()

@app.get("/", status_code=201)
def helloWorld():
    return f"Hello world"


@app.post("/users/", status_code=201)
def register_user(user_data: dict):
    username = user_data.get("username")
    password = user_data.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username e senha são obrigatórios")

    return create_user(username, password)

@app.get("/users/")
def list_users():
    return get_all_users()
