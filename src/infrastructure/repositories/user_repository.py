from typing import List
from src.domain.entities.user import User
from src.infrastructure import Context, context


class UserRepository:
    context: Context

    def __init__(self):
        self.context = context

    def get_all(self) -> List[User]:
        return self.context.query(User).all()

    def query(self) -> List[User]:
        return self.context.query(User)

    def add(self, user: User) -> None:
        user.encode_password()
        self.context.add(user)
        self.context.commit()
