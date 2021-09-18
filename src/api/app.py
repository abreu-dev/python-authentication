from fastapi import FastAPI
from src.api.controllers import api_router

app = FastAPI()


@app.get("/api")
async def main():
    return {"message": "Hello World"}

app.include_router(api_router)
