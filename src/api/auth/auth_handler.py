from jwt import encode, decode
from time import time
from typing import Dict


JWT_SECRET = "deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f"
JWT_ALGORITHM = "HS256"


def get_full_token(user) -> Dict[str, str]:
    payload = {"sub": str(user.id),
               "email": user.email,
               "exp": time() + (60 * 60 * 24),
               "iss": "AuthenticationPython",
               "aud": "AuthenticationPython"
               }
    return encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    decoded_token = decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token["exp"] >= time() else None


def verify_jwt(token: str) -> bool:
    if decode_token(token):
        return True
    return False



