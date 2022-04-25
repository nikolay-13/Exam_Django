import random

from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.db import models

from Exam_Django.common import choices
from Exam_Django.store.model_utils import validators


def create_new_ref_number():
    return 'PDN#' + str(random.randint(1000000000, 9999999999))


class Product(models.Model):
    _ERROR_FIELD_TITLE = 'title'
    _ERROR_FIELD_BRAND = 'brand'
    _TITLE_MIN_LENGTH = 2
    _TITLE_MAX_LENGTH = 20
    _BRAND_MIN_LENGTH = 2
    _BRAND_MAX_LENGTH = 20
    _MIN_QNT = 0
    _MIN_PRICE = 0
    _ID_MAX_LENGTH = 16
    _PRICE_DEFAULT = 0
    _QNT_DEFAULT = 0
    _BRAND_DEFAULT = 'no brand'
    _BRAND_ERROR_MSG = f'Ensure brand contain only letters, dashes or backslash.\n Ensure title not exceed {_BRAND_MAX_LENGTH} characters'
    _TITLE_ERROR_MSG = f'Ensure title contain only letters, dashes or backslash.\n Ensure title not exceed {_TITLE_MAX_LENGTH} characters'
    product_id = models.CharField(
        primary_key=True,
        max_length=_ID_MAX_LENGTH,
        blank=False,
        editable=False,
        unique=True,
        default=create_new_ref_number
    )
    title = models.CharField(
        max_length=_TITLE_MAX_LENGTH,
        blank=False,
        null=False,
        validators=(
            validators.NameValidator(min_length=_TITLE_MIN_LENGTH,
                                     max_length=_TITLE_MAX_LENGTH,
                                     field=_ERROR_FIELD_TITLE,
                                     msg=_TITLE_ERROR_MSG),
        )
    )
    price = models.FloatField(
        blank=False,
        null=False,
        default=_PRICE_DEFAULT,
        validators=(
            MinValueValidator(_MIN_PRICE),
        )
    )
    description = models.TextField(
        blank=False,
        null=False
    )
    av_qnt = models.IntegerField(
        default=_QNT_DEFAULT,
        validators=(
            MinValueValidator(_MIN_QNT),
        )

    )
    brand = models.CharField(
        max_length=_BRAND_MAX_LENGTH,
        default=_BRAND_DEFAULT,
        validators=(
            validators.NameValidator(min_length=_BRAND_MIN_LENGTH,
                                     max_length=_BRAND_MAX_LENGTH,
                                     field=_ERROR_FIELD_BRAND,
                                     msg=_BRAND_ERROR_MSG),
        )
    )


class ProductSizes(models.Model):
    _RELATED_NAME = 'size'
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name=_RELATED_NAME,
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
    _RELATED_NAME = 'color'
    _COLOR_MIN_LENGTH = 1
    _COLOR_ERROR_MSG = f'Ensure color contain only letters, dashes or backslash.\n Ensure title not exceed {_COLOR_MAX_LENGTH} characters'
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name=_RELATED_NAME,
    )
    color = models.CharField(
        max_length=_COLOR_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(validators.NameValidator(max_length=_COLOR_MAX_LENGTH,
                                             min_length=_COLOR_MIN_LENGTH,
                                             field=_RELATED_NAME,
                                             msg=_COLOR_ERROR_MSG),)
    )

    def __str__(self):
        return self.color


class ProductCategory(models.Model):
    _RELATED_NAME = 'category'
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name=_RELATED_NAME
    )
    category = models.CharField(
        max_length=max((len(x) for x, _ in choices.CATEGORY)),
        null=False,
        blank=False,
        choices=choices.CATEGORY,
    )


class ProductGender(models.Model):
    _RELATED_NAME = 'gender'
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name=_RELATED_NAME
    )
    gender = models.CharField(
        max_length=max((len(x) for x, _ in choices.GENDER)),
        choices=choices.GENDER,
    )


class ProductPictures(models.Model):
    _MAX_WIDTH = 480
    _MAX_HEIGHT = 640
    _RELATED_NAME = 'pictures'
    _UPLOAD_TO = 'products/'
    _FORMAT = "webp"
    product_id = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        unique=False,
        related_name=_RELATED_NAME,
    )

    picture = CloudinaryField('picture',
                              transformation={'width': f'{_MAX_WIDTH}', 'height': f'{_MAX_HEIGHT}', 'crop': 'fill',
                                              'radius': '20'},
                              folder=f'/e-com/products/{product_id}', format={_FORMAT},)
