from pydantic import BaseModel


class RegisterUserModel(BaseModel):
    email: str
    username: str
    password: str
