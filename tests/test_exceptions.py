import pytest
from formidable.exceptions import (
    ValidationError,
    EmailError,
    PasswordError,
    FieldRequiredError,
    SelectFieldError,
)


def test_validation_error():
    with pytest.raises(ValidationError):
        raise ValidationError("Validation error")


def test_email_error():
    with pytest.raises(EmailError):
        raise EmailError("Email error")


def test_password_error():
    with pytest.raises(PasswordError):
        raise PasswordError("Password error")


def test_field_required_error():
    with pytest.raises(FieldRequiredError):
        raise FieldRequiredError("Field required error")


def test_select_field_error():
    with pytest.raises(SelectFieldError):
        raise SelectFieldError("Select field error")
