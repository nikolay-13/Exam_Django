# Generated by Django 4.0.3 on 2022-04-08 16:52

import Exam_Django.accounts.model_utils.validators
import Exam_Django.accounts.models.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/profile_pics')),
                ('first_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), Exam_Django.accounts.model_utils.validators.name_validator])),
                ('last_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), Exam_Django.accounts.model_utils.validators.name_validator])),
                ('tel_number', models.CharField(max_length=10, unique=True, validators=[Exam_Django.accounts.model_utils.validators.tel_validator])),
                ('ref_num', models.CharField(default=Exam_Django.accounts.models.models.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
