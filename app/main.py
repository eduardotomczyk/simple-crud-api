from fastapi import FastAPI

app = FastAPI(title="Simple CRUD API")


@app.get("/")
def root():
    return {"message": "API is running 🚀"}