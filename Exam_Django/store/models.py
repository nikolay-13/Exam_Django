import random

from django.db import models

from Exam_Django.common.image_resize import image_resize


def create_new_ref_number():
    return 'PDN#' + str(random.randint(1000000000, 9999999999))


class Product(models.Model):
    product_id = models.CharField(
        primary_key=True,
        max_length=16,
        blank=False,
        editable=False,
        unique=True,
        default=create_new_ref_number
    )
    title = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    price = models.IntegerField(
        blank=False,
        null=False,
        default=0,
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    av_qnt = models.IntegerField(
        default=0,

    )
    brand = models.CharField(
        max_length=30,
        default='No brand',
    )


class ProductSizes(models.Model):
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name='size',
    )
    size = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )


class ProductColors(models.Model):
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name='color',
    )
    color = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )


class ProductCategory(models.Model):
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name='category'
    )
    category = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )


class ProductGender(models.Model):
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name='gender'
    )
    gender = models.CharField(
        max_length=20,
    )


class ProductPictures(models.Model):
    _MAX_WIDTH = 480
    _MAX_HEIGHT = 640
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name='pictures',
    )

    picture = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super(ProductPictures, self).save(*args, **kwargs)

        img = image_resize(self.picture, self._MAX_WIDTH, self._MAX_HEIGHT)
