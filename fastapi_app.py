# fastapi_app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/fastapi")
def fastapi():
    return {"message": "Hello from FastAPI!"}
@app.get("/demo")
def fastapi():
    return {"message": "Hello from Jayashree!"}

