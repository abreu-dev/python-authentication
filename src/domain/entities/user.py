from sqlalchemy import Column, String
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from uuid import uuid4
from src.infrastructure import Base
from src.infrastructure.crypto import encode_password


class User(Base):
    __tablename__ = "users"

    id = Column(UNIQUEIDENTIFIER, default=lambda: uuid4(), primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def encode_password(self):
        self.password = encode_password(self.password)

