import random

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from Exam_Django.accounts.model_utils.validators import tel_validator, name_validator
from Exam_Django.common.image_resize import image_resize

UserModel = get_user_model()


def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999))


class Profile(models.Model):
    _MAX_WIDTH = 100
    _MAX_HEIGHT = 100
    _FIRST_NAME_MAX_LENGTH = 20
    _LAST_NAME_MAX_LENGTH = 20
    _FIRST_NAME_MIN_LENGTH = 2
    _LAST_NAME_MIN_LENGTH = 2
    _TEL_MAX_LENGTH = 10
    profile_picture = models.ImageField(
        upload_to='media/profile_pics',
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=_FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(_FIRST_NAME_MIN_LENGTH),
            name_validator,
        )
    )
    last_name = models.CharField(
        max_length=_LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(_LAST_NAME_MIN_LENGTH),
            name_validator,
        )
    )
    tel_number = models.CharField(
        max_length=_TEL_MAX_LENGTH,
        unique=True,
        validators=(
            tel_validator,
            # validators.MinLengthValidator(_TEL_MIN_LENGTH),
        )
    )
    ref_num = models.CharField(
        max_length=10,
        blank=False,
        editable=False,
        unique=True,
        default=create_new_ref_number
    )
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = image_resize(self.profile_picture, self._MAX_WIDTH, self._MAX_HEIGHT)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
