from jwt import encode, decode
from time import time
from typing import Dict


JWT_SECRET = "843c3415-a4f5-4b05-8601-d8c827fb0e9d"
JWT_ALGORITHM = "HS256"


def get_full_token(user) -> Dict[str, str]:
    payload = {"sub": user.id,
               "email": user.email,
               "exp": time() + (60 * 60 * 24),
               "iss": "AuthenticationPython",
               "aud": "AuthenticationPython"
               }
    return encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> dict:
    decoded_token = decode(token, JWT_SECRET, audience="AuthenticationPython", algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token["exp"] >= time() else None


def verify_jwt(token: str) -> bool:
    if decode_token(token):
        return True
    return False



