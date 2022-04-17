from django import forms

from django.utils.safestring import mark_safe

from Exam_Django.store.models import Product, ProductCategory, ProductSizes, ProductGender, ProductColors, \
    ProductPictures
from Exam_Django.common import choices


class ProductMainForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request') if 'request' in kwargs else None
        super(ProductMainForm, self).__init__(*args, **kwargs)

    _COLOR_FIELD_MAX_LEN = 20
    _IMAGE_MESSAGE = 'Image was invalid'
    images = forms.ImageField(
        widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    category = forms.ChoiceField(
        choices=choices.CATEGORY,
    )
    size = forms.MultipleChoiceField(choices=choices.SIZES, widget=forms.CheckboxSelectMultiple())
    gender = forms.ChoiceField(
        choices=choices.GENDER,
    )
    color = forms.CharField(
        max_length=_COLOR_FIELD_MAX_LEN,
    )

    class Meta:
        model = Product
        exclude = ('av_qnt',)

    def save(self, commit=True):
        product = super(ProductMainForm, self).save(commit=commit)
        if commit:
            product.save()
            images = self.request.FILES.getlist('images')
            sizes = self.cleaned_data['size']
            ProductCategory.objects.update_or_create(
                product_id=product,
                category=self.cleaned_data['category']
            )
            for size in sizes:
                if size not in product.size.all():
                    product.av_qnt += 1
                    product.save()
                    ProductSizes.objects.update_or_create(
                        product_id=product,
                        size=size
                    )
            ProductGender.objects.update_or_create(
                product_id=product,
                gender=self.cleaned_data['gender']
            )
            ProductColors.objects.update_or_create(
                product_id=product,
                color=self.cleaned_data['color']
            )
            for img in images:
                ProductPictures.objects.create(
                    product_id=product,
                    picture=img
                )
        return product


class ImagePreviewWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        img_html = mark_safe(f'<img src="{value.url}"style="width:100px;height:100px"/><br>')
        return f'{input_html}{img_html}'


class EditProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request') if 'request' in kwargs else None
        self.item = kwargs.pop('product') if 'product' in kwargs else None
        super(EditProductForm, self).__init__(*args, **kwargs)

        for img in self.item.pictures.all():
            self.fields[img.picture.name] = forms.ImageField(
                initial=img.picture, widget=ImagePreviewWidget(),
                label=f'current: {img.picture.name.split(".")[-2]}'
            )

    add_images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': 'multiple'}), required=False)

    class Meta:
        model = Product
        exclude = ('images', 'brand', 'av_qnt')

    def save(self, commit=True):
        item = super(EditProductForm, self).save(commit=commit)
        images = ProductPictures.objects.filter(product_id=item)
        new_images = self.request.FILES.getlist('add_images')
        for img in images:
            img.picture = self.cleaned_data[img.picture.name]
            img.save()
        if new_images:
            for img in new_images:
                ProductPictures.objects.create(

                    product_id=item,
                    picture=img
                )
        if commit:
            item.save()
