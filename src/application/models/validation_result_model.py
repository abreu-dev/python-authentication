from pydantic import BaseModel
from typing import List


class ValidationResultModel(BaseModel):
    is_valid: bool = True
    errors: List[str] = []

    def add_error(self, error: str) -> None:
        self.errors.append(error)
        self.is_valid = False
