from fastapi import FastAPI
from app.db.session import SessionLocal
from app import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}