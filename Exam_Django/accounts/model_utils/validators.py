import re

from django.core.exceptions import ValidationError


def tel_validator(value):
    if not re.match(r'^[0-9]{10}$', value):
        raise ValidationError('Ensure number you entered a valid number.')


def name_validator(value):
    if not re.match(r'^[A-z]*$', value):
        raise ValidationError('Ensure your name contains only letters.')
