from fastapi import APIRouter
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from uuid import uuid4
from src.api.auth.auth_handler import get_full_token
from src.application.models.login_user_model import LoginUserModel
from src.application.models.register_user_model import RegisterUserModel
from src.application.models.validation_result_model import ValidationResultModel
from src.domain.entities.user import User
from src.infrastructure.crypto import encode_password
from src.infrastructure.repositories.user_repository import UserRepository

router = APIRouter()


@router.post("/register")
async def register(register_user_model: RegisterUserModel):
    user_repository = UserRepository()
    validation_result = ValidationResultModel()

    if user_repository.query() \
            .filter_by(username=register_user_model.username) \
            .first() is not None:
        validation_result.add_error(f"Username '{register_user_model.username}' is already taken.")

    if user_repository.query() \
            .filter_by(email=register_user_model.email) \
            .first() is not None:
        validation_result.add_error(f"Email '{register_user_model.email}' is already taken.")

    if validation_result.errors:
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={"errors": validation_result.errors})

    user = User(id=uuid4(),
                email=register_user_model.email,
                username=register_user_model.username,
                password=register_user_model.password)
    user_repository.add(user)

    return JSONResponse(status_code=HTTP_200_OK,
                        content={"accessToken": get_full_token(user),
                                 "username": user.username,
                                 "email": user.email})


@router.post("/login")
async def login(login_user_model: LoginUserModel):
    user_repository = UserRepository()
    validation_result = ValidationResultModel()

    user = user_repository.query() \
        .filter_by(username=login_user_model.username,
                   password=encode_password(login_user_model.password)) \
        .one_or_none()

    if user is None:
        validation_result.add_error("Incorrect username or password.")
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={"errors": validation_result.errors})

    return JSONResponse(status_code=HTTP_200_OK,
                        content={"accessToken": get_full_token(user),
                                 "username": user.username,
                                 "email": user.email})
