from django.contrib import admin

from django.contrib.admin import ModelAdmin
from django.utils.html import format_html

from Exam_Django.staff_app.Forms.product_main_form import ProductMainForm
from Exam_Django.store.models import Product


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
