import secrets
import logging
from typing import Protocol
from .exceptions import ValidationError

# Configure logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

class CSRFStorage(Protocol):
    def __getitem__(self, key: str) -> str:
        ...

    def __setitem__(self, key: str, value: str) -> None:
        ...

class CSRF:
    def __init__(self, storage: CSRFStorage):
        self.storage = storage

    def generate_token(self) -> str:
        token = secrets.token_urlsafe(32)
        self.storage['csrf_token'] = token
        return token

    def validate_token(self, token: str) -> None:
        try:
            stored_token = self.storage['csrf_token']
        except KeyError:
            logger.warning("CSRF token has not been set.")
            raise ValidationError("CSRF token is missing")
        
        if token != stored_token:
            raise ValidationError("Invalid CSRF token")