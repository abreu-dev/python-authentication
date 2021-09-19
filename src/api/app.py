from fastapi import FastAPI
from src.api.controllers import api_router
from src.domain.entities import user
from src.infrastructure import engine

user.Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/api")
async def main():
    return {"message": "Hello World"}

app.include_router(api_router)
