from fastapi import APIRouter
from src.api.controllers.health_check_controller import router as health_check_router
from src.api.controllers.account_controller import router as account_check_router

api_router = APIRouter()
api_router.include_router(health_check_router, prefix="/api/healthcheck")
api_router.include_router(account_check_router, prefix="/api/accounts")
