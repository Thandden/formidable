import pytest
from formidable.forms import Form
from formidable.csrf import CSRF
from formidable.exceptions import ValidationError, EmailError, PasswordError
from formidable.validators import EmailValidator, PasswordValidator, PasswordMatchValidator, PasswordCharsValidator, FieldRequiredValidator, SelectFieldValidator
from typing import List
class MockStorage:
    def __init__(self):
        self.storage = {}

    def __getitem__(self, key: str) -> str:
        return self.storage.get(key, '')

    def __setitem__(self, key: str, value: str) -> None:
        self.storage[key] = value

class MockEmailForm(Form):
    def get_validators(self) -> List[EmailValidator]:
        email = self.form_data.get('email', '')
        return [EmailValidator(email)]

class MockContactForm(Form):
    select_options = ['option1', 'option2', 'option3']

    def get_validators(self) -> List:
        email = self.form_data.get('email', '')
        password = self.form_data.get('password', '')
        confirm_password = self.form_data.get('confirmPassword', '')
        terms = self.form_data.get('terms', '')
        select_field = self.form_data.get('selectField', '')
        standard_field = self.form_data.get('standardField', '')
        return [
            EmailValidator(email),
            PasswordValidator(password),
            PasswordMatchValidator(password, confirm_password),
            PasswordCharsValidator(password),
            FieldRequiredValidator(terms, "Terms and Conditions"),
            SelectFieldValidator(select_field, self.select_options, "Select Field"),
            FieldRequiredValidator(standard_field, "Standard Field")
        ]

def test_email_form():
    storage = MockStorage()
    csrf = CSRF(storage)
    csrf.generate_token()
    form_data = {'email': 'test@example.com', 'csrf_token': storage['csrf_token']}
    form = MockEmailForm(form_data, csrf)
    errors = form.validate()
    assert not errors  # No errors should be present

    invalid_form_data = {'email': 'invalid-email', 'csrf_token': storage['csrf_token']}
    invalid_form = MockEmailForm(invalid_form_data, csrf)
    errors = invalid_form.validate()
    assert 'email_error' in errors  # Email validation should fail

def test_contact_form():
    storage = MockStorage()
    csrf = CSRF(storage)
    csrf.generate_token()
    form_data = {
        'email': 'test@example.com',
        'password': 'Password1!',
        'confirmPassword': 'Password1!',
        'terms': 'accepted',
        'selectField': 'option1',
        'standardField': 'value',
        'csrf_token': storage['csrf_token']
    }
    form = MockContactForm(form_data, csrf)
    errors = form.validate()
    assert not errors  # No errors should be present

    invalid_form_data = form_data.copy()
    invalid_form_data['email'] = 'invalid-email'
    invalid_form = MockContactForm(invalid_form_data, csrf)
    errors = invalid_form.validate()
    assert 'email_error' in errors  # Email validation should fail