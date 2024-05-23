import re
from abc import ABC, abstractmethod
from typing import List, Optional
from .exceptions import EmailError, PasswordError, FieldRequiredError, SelectFieldError


class Validator(ABC):
    @abstractmethod
    def validate(self) -> None:
        pass


class EmailValidator(Validator):
    def __init__(self, email: str):
        self.email = email

    def validate(self) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise EmailError("Invalid email address")


class PasswordValidator(Validator):
    def __init__(self, password: str):
        self.password = password

    def validate(self) -> None:
        if len(self.password) < 8:
            raise PasswordError("Password must be at least 8 characters long")


class PasswordMatchValidator(Validator):
    def __init__(self, password: str, confirm_password: str):
        self.password = password
        self.confirm_password = confirm_password

    def validate(self) -> None:
        if self.password != self.confirm_password:
            raise PasswordError("Passwords do not match")


class PasswordCharsValidator(Validator):
    def __init__(self, password: str):
        self.password = password

    def validate(self) -> None:
        checks = [
            (r"[A-Z]", "Password must contain at least one uppercase letter"),
            (r"[a-z]", "Password must contain at least one lowercase letter"),
            (r"[0-9]", "Password must contain at least one digit"),
            (r"[\W_]", "Password must contain at least one special character"),
        ]

        errors = [
            error_message
            for pattern, error_message in checks
            if not re.search(pattern, self.password)
        ]

        if errors:
            raise PasswordError("; ".join(errors))


class FieldRequiredValidator(Validator):
    def __init__(self, field_value: str, field_name: str):
        self.field_value = field_value
        self.field_name = field_name

    def validate(self) -> None:
        if not self.field_value:
            raise FieldRequiredError(f"{self.field_name} is required")


class SelectFieldValidator(Validator):
    def __init__(self, field_value: str, valid_options: List[str], field_name: str):
        self.field_value = field_value
        self.valid_options = valid_options
        self.field_name = field_name

    def validate(self) -> None:
        if self.field_value not in self.valid_options:
            raise SelectFieldError(f"Invalid selection for {self.field_name}")

class OptionalFieldValidator(Validator):
    def __init__(self, field_value: Optional[str], field_name: Optional[str]):
        self.field_value = field_value
        self.field_name = field_name
    
    def validate(self) -> None:
        pass