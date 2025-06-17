from fastapi import FastAPI
from routes.routes import router as routes_users

app = FastAPI()

@app.get("/", status_code=201)
def helloWorld():
    return f"Hello world"

app.include_router(routes_users)


