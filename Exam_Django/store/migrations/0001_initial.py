# Generated by Django 4.0.3 on 2022-04-08 16:02

import Exam_Django.store.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.CharField(default=Exam_Django.store.models.create_new_ref_number, editable=False, max_length=16, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=20)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('av_qnt', models.IntegerField(default=0)),
                ('brand', models.CharField(default='No brand', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='size', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=20)),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='gender', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('product_id', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='store.product')),
            ],
        ),
    ]