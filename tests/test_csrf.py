import pytest
from formidable.csrf import CSRF
from formidable.exceptions import ValidationError


class MockStorage:
    def __init__(self):
        self.storage = {}

    def __getitem__(self, key: str) -> str:
        return self.storage.get(key, "")

    def __setitem__(self, key: str, value: str) -> None:
        self.storage[key] = value


def test_csrf_generate_token():
    storage = MockStorage()
    csrf = CSRF(storage)
    token = csrf.generate_token()
    assert token == storage["csrf_token"]


def test_csrf_validate_token():
    storage = MockStorage()
    csrf = CSRF(storage)
    token = csrf.generate_token()
    csrf.validate_token(token)

    with pytest.raises(ValidationError):
        csrf.validate_token("invalid_token")
