import re

from django.core.exceptions import ValidationError


class NameValidator:
    def __init__(self, min_length, max_length, field, msg):
        self.msg = msg
        self.field = field
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        exp = r'^[a-zA-Z-\\ ]{' + str(self.min_length) + ',' + str(self.max_length) + '}$'
        if not re.match(exp, value):
            raise ValidationError(self.msg)
        else:
            return value
