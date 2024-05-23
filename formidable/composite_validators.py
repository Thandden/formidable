from typing import List, Optional
from .validators import Validator, PasswordValidator, PasswordCharsValidator


class CompositePasswordValidator(Validator):
    def __init__(self, password: str, validators: Optional[List[Validator]] = None):
        self.password = password
        self.validators = validators or self.get_validators()

    def get_validators(self) -> List[Validator]:
        return [
            PasswordValidator(self.password),
            PasswordCharsValidator(self.password),
            # Add more default validators if needed
        ]

    def validate(self) -> None:
        [validator.validate() for validator in self.validators]
