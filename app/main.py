from fastapi import FastAPI
from .routes import items

app = FastAPI(title="Simple CRUD API")

app.include_router(items.router)


@app.get("/")
def root():
    return {"message": "API is running 🚀"}