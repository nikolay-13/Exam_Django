import random

from django.core.validators import MinValueValidator
from django.db import models

from Exam_Django.common import choices
from Exam_Django.common.image_resize import image_resize


def create_new_ref_number():
    return 'PDN#' + str(random.randint(1000000000, 9999999999))


class Product(models.Model):
    _MIN_QNT = 0
    _MIN_PRICE = 0
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
    price = models.FloatField(
        blank=False,
        null=False,
        default=0,
        validators=(
            MinValueValidator(_MIN_PRICE),
        )
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    av_qnt = models.IntegerField(
        default=0,
        validators=(
            MinValueValidator(_MIN_QNT),
        )

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
        max_length=max((len(x) for x, _ in choices.SIZES)),
        null=False,
        blank=False,
        choices=choices.SIZES,
    )
    def __str__(self):
        return self.size


class ProductColors(models.Model):
    _COLOR_MAX_LENGTH = 20
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
        max_length=_COLOR_MAX_LENGTH,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.color


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
        max_length=max((len(x) for x, _ in choices.CATEGORY)),
        null=False,
        blank=False,
        choices=choices.CATEGORY,
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
        max_length=max((len(x) for x, _ in choices.GENDER)),
        choices=choices.GENDER,
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
        return img

    def __str__(self):
        return self.picture
