from django import forms
from django.contrib.admin import ModelAdmin

from Exam_Django.store.models import Product, ProductCategory, ProductSizes, ProductGender, ProductColors, \
    ProductPictures
from Exam_Django.common import choices


class ProductMainForm(forms.ModelForm):
    images = forms.ImageField(
    )
    category = forms.ChoiceField(
        choices=choices.CATEGORY,
    )
    size = forms.ChoiceField(
        choices=choices.SIZES,
    )
    gender = forms.ChoiceField(
        choices=choices.GENDER,
    )
    color = forms.CharField(
        max_length=10,
    )

    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        product = super(ProductMainForm, self).save(commit=commit)
        if commit:
            product.save()
            ProductCategory.objects.update_or_create(
                product_id=product,
                category=self.cleaned_data['category']
            )
            ProductSizes.objects.update_or_create(
                product_id=product,
                size=self.cleaned_data['size']
            )
            ProductGender.objects.update_or_create(
                product_id=product,
                gender=self.cleaned_data['gender']
            )
            ProductColors.objects.update_or_create(
                product_id=product,
                color=self.cleaned_data['color']
            )
            ProductPictures.objects.update_or_create(
                product_id=product,
                picture=self.cleaned_data['images']
            )
        return product


