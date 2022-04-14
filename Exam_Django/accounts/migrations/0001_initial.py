# Generated by Django 4.0.3 on 2022-04-14 18:21

import Exam_Django.accounts.model_utils.validators
import Exam_Django.accounts.models.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='media/profile_pics')),
                ('first_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), Exam_Django.accounts.model_utils.validators.name_validator])),
                ('last_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), Exam_Django.accounts.model_utils.validators.name_validator])),
                ('tel_number', models.CharField(max_length=10, validators=[Exam_Django.accounts.model_utils.validators.tel_validator])),
                ('ref_num', models.CharField(default=Exam_Django.accounts.models.models.create_new_ref_number, editable=False, max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('tel_number', 'ref_num')},
            },
        ),
    ]
