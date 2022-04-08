from django.contrib.auth import base_user
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from Exam_Django.accounts.managers import UserProfileManager


class UserProfile(base_user.AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = 'email'
    is_staff = models.BooleanField(
        default=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    objects = UserProfileManager()
