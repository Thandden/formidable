import pytest
from formidable.validators import (
    EmailValidator,
    PasswordValidator,
    PasswordMatchValidator,
    PasswordCharsValidator,
    FieldRequiredValidator,
    SelectFieldValidator,
)
from formidable.exceptions import (
    EmailError,
    PasswordError,
    FieldRequiredError,
    SelectFieldError,
)


def test_email_validator():
    validator = EmailValidator("test@example.com")
    validator.validate()

    with pytest.raises(EmailError):
        invalid_validator = EmailValidator("invalid-email")
        invalid_validator.validate()


def test_password_validator():
    validator = PasswordValidator("strongpassword")
    validator.validate()

    with pytest.raises(PasswordError):
        short_password_validator = PasswordValidator("short")
        short_password_validator.validate()


def test_password_match_validator():
    validator = PasswordMatchValidator("password123", "password123")
    validator.validate()

    with pytest.raises(PasswordError):
        mismatch_validator = PasswordMatchValidator("password123", "password321")
        mismatch_validator.validate()


def test_password_chars_validator():
    validator = PasswordCharsValidator("Password1!")
    validator.validate()

    with pytest.raises(PasswordError):
        no_uppercase_validator = PasswordCharsValidator("password1!")
        no_uppercase_validator.validate()

    with pytest.raises(PasswordError):
        no_digit_validator = PasswordCharsValidator("Password!")
        no_digit_validator.validate()

    with pytest.raises(PasswordError):
        no_special_char_validator = PasswordCharsValidator("Password1")
        no_special_char_validator.validate()


def test_field_required_validator():
    validator = FieldRequiredValidator("value", "Field")
    validator.validate()

    with pytest.raises(FieldRequiredError):
        empty_validator = FieldRequiredValidator("", "Field")
        empty_validator.validate()


def test_select_field_validator():
    validator = SelectFieldValidator("option1", ["option1", "option2"], "Select Field")
    validator.validate()

    with pytest.raises(SelectFieldError):
        invalid_option_validator = SelectFieldValidator(
            "invalid", ["option1", "option2"], "Select Field"
        )
        invalid_option_validator.validate()
