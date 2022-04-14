from django.contrib import admin
from django.contrib.auth import get_user_model

from Exam_Django.accounts.models.models import Profile

UserModel = get_user_model()
admin.site.register(UserModel)
