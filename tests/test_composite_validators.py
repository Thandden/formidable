import pytest
from formidable.composite_validators import CompositePasswordValidator
from formidable.exceptions import PasswordError

def test_composite_password_validator():
    validator = CompositePasswordValidator("Password1!")
    validator.validate()

    with pytest.raises(PasswordError):
        invalid_validator = CompositePasswordValidator("password")
        invalid_validator.validate()