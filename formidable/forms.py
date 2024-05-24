from abc import ABC, abstractmethod
from typing import Dict, Any, List, Tuple
from .validators import Validator
from .csrf import CSRF
from .exceptions import ValidationError

class Form(ABC):
    def __init__(self, form_data: Dict[str, Any], csrf: CSRF):
        self.form_data: Dict[str, Any] = form_data
        self.csrf = csrf
        self.validators: List[Validator] = self.get_validators()

    @abstractmethod
    def get_validators(self) -> List[Validator]:
        pass

    def validate(self) -> Dict[str, str]:
        errors: Dict[str, str]
        errors = {}
        csrf_token: str = self.form_data.get('csrf_token', '')
        if not csrf_token:
            errors['csrf_token'] = "CSRF token is missing"
        else:
            try:
                self.csrf.validate_token(csrf_token)
            except ValidationError as e:
                errors['csrf_token'] = str(e)

        for validator in self.validators:
            try:
                validator.validate()
            except ValidationError as e:
                field_name = validator.__class__.__name__.replace('Validator', '').lower()
                errors[f"{field_name}_error"] = str(e)

        return errors
