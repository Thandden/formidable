class ValidationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class EmailError(ValidationError):
    pass


class PasswordError(ValidationError):
    pass


class FieldRequiredError(ValidationError):
    pass


class SelectFieldError(ValidationError):
    pass

class CustomError(ValidationError):
    pass