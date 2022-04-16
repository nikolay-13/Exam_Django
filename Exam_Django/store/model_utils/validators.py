import re

from django.core.exceptions import ValidationError


class NameValidator:
    def __init__(self, min_length, max_length, field, msg):
        self.msg = msg
        self.field = field
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        if not re.match(fr'^[a-zA-Z-/]{self.min_length,self.max_length}$', value):
            raise ValidationError(self.msg)
        return value
