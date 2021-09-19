from base64 import b64encode


def encode_password(password: str) -> str:
    return b64encode(password.encode("utf-8"))
