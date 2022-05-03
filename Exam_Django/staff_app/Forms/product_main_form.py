import cloudinary.uploader
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
    _MAX_WIDTH = 480
    _MAX_HEIGHT = 640
    _UPLOAD_TO = 'products/'
    _FORMAT = "webp"
    _IMAGE_MESSAGE = 'Image was invalid'
    ob_image = forms.ImageField(
        # widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    image1 = forms.ImageField(
        # widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    image2 = forms.ImageField(
        # widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    image3 = forms.ImageField(
        # widget=forms.FileInput(attrs={'multiple': 'multiple'}),
        required=False,
    )
    image4 = forms.ImageField(
        # widget=forms.FileInput(attrs={'multiple': 'multiple'}),
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
            images = ('ob_image',
                      'image1',
                      'image2',
                      'image3',
                      'image4',)
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
                if img in self.request.FILES:
                    ProductPictures.objects.create(
                        product_id=product,
                        picture=cloudinary.uploader.upload_image(self.request.FILES[img],
                                                                 transformation={'width': f'{self._MAX_WIDTH}',
                                                                                 'height': f'{self._MAX_HEIGHT}',
                                                                                 'aspect-ratio': '1.1',
                                                                                 'radius': '20'},
                                                                 folder=f'e-com/products/',
                                                                 format=self._FORMAT, )
                    )
        return product


class ImagePreviewWidget(forms.widgets.ClearableFileInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super().render(name, value, attrs=None, **kwargs)
        if value:
            img_html = mark_safe(f'<img src="{value}"style="width:100px;height:100px"/><br>')
        else:
            img_html = None
        return f'{img_html}Change:{input_html}'


class EditProductForm(forms.ModelForm):
    _MAX_WIDTH = 480
    _MAX_HEIGHT = 640
    _UPLOAD_TO = 'products/'
    _FORMAT = "webp"
    _IMAGE_MESSAGE = 'Image was invalid'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request') if 'request' in kwargs else None
        self.item = kwargs.pop('product') if 'product' in kwargs else None
        super(EditProductForm, self).__init__(*args, **kwargs)
        self.fields['image0'].label = ''
        self.fields['image1'].label = ''
        self.fields['image2'].label = ''
        self.fields['image3'].label = ''
        self.fields['image4'].label = ''

    image0 = forms.FileField(
        widget=ImagePreviewWidget(),
        required=False,

    )
    image1 = forms.ImageField(
        widget=ImagePreviewWidget(),
        required=False,
    )
    image2 = forms.ImageField(
        widget=ImagePreviewWidget(),
        required=False,
    )
    image3 = forms.ImageField(
        widget=ImagePreviewWidget(),
        required=False,
    )
    image4 = forms.ImageField(
        widget=ImagePreviewWidget(),
        required=False,
    )

    class Meta:
        model = Product
        exclude = ('images', 'brand', 'av_qnt')
