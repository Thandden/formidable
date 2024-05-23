from .csrf import CSRFStorage
from flask import session

class FlaskSessionStorage(CSRFStorage):
    def __getitem__(self, key: str) -> str:
        return session.get(key, '')

    def __setitem__(self, key: str, value: str) -> None:
        session[key] = value
