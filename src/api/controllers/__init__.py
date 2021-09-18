from fastapi import APIRouter
from src.api.controllers.health_check_controller import router as health_check_router

api_router = APIRouter()
api_router.include_router(health_check_router, prefix="/api/healthcheck")
