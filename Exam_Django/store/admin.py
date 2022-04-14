from django.contrib import admin

from django.contrib.admin import ModelAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy

from Exam_Django.store.Forms.product_main_form import ProductMainForm
from Exam_Django.store.models import Product, ProductSizes, ProductColors, ProductGender, ProductCategory, \
    ProductPictures


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    def image_tag(self, obj):
        if obj.pictures:
            for pic in obj.pictures.all():
                return format_html('<img src="{}" style = "width: 150px; height:150px;"/>'.format(pic.picture.url))
        return 'N/A'

    image_tag.short_description = 'Image'

    list_display = (
        'product_id',
        'title',
        'brand',
        'price',
        'image_tag'
    )
    image_tag.empty_value_display = 'N/A'
    form = ProductMainForm
    add_form = ProductMainForm

    def get_form(self, request, obj=None, **kwargs):
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        else:
            if obj.pictures.count() > 0:
                for pic in obj.pictures.all():
                    defaults['form'] = self.add_form
                    defaults['form'].base_fields['images'].initial = pic.picture

                    break
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    # def save_model(self, request, obj, form, change):
    #     super(ProductAdmin, self).save_model(request, obj, form, change)
    #     try:
    #         obj.category.get(category=form.cleaned_data['category'])
    #         obj.category = form.cleaned_data['category']
    #     except obj.DoesNotExist:
    #
    #         ProductCategory.objects.create(
    #             product_id=obj,
    #             category=form.cleaned_data['category']
    #         )
    #     try:
    #         obj.size.get(size=form.cleaned_data['size'])
    #     except obj.DoesNotExist:
    #         ProductSizes.objects.create(
    #             product_id=obj,
    #             size=form.cleaned_data['size']
    #         )
    #     try:
    #         obj.gender.get(gender=form.cleaned_data['gender'])
    #         obj.gender = form.cleaned_data['gender']
    #     except obj.DoesNotExist:
    #         ProductGender.objects.create(
    #             product_id=obj,
    #             gender=form.cleaned_data['gender']
    #         )
    #     try:
    #         obj.color.get(color=form.cleaned_data['color'])
    #     except obj.DoesNotExist:
    #         ProductColors.objects.create(
    #             product_id=obj,
    #             color=form.cleaned_data['color']
    #         )
    #     try:
    #         obj.pictures.get(picture=form.cleaned_data['images'])
    #     except DoesNotExist:
    #         ProductPictures.objects.create(
    #             product_id=obj,
    #             picture=form.cleaned_data['images']
    #         )
    #     obj.save()
