from django import forms

from Exam_Django.store.models import Product, ProductCategory, ProductSizes, ProductGender, ProductColors, ProductPictures


class ProductMainForm(forms.ModelForm):
    images = forms.ImageField(
    )
    category = forms.CharField(
        max_length=30,
    )
    size = forms.CharField(
        max_length=30,
    )
    gender = forms.CharField(
        max_length=30,
    )
    color = forms.CharField(
        max_length=30,
    )
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        product = super(ProductMainForm, self).save(commit=commit)
        if commit:
            product.save()
            ProductCategory.objects.create(
                product_id=product,
                category=self.cleaned_data['category']
            )
            for size in self.cleaned_data['size'].split('/'):
                ProductSizes.objects.create(
                    product_id=product,
                    size=size
                )
            ProductGender.objects.create(
                product_id=product,
                gender=self.cleaned_data['gender']
            )
            ProductColors.objects.create(
                product_id=product,
                color=self.cleaned_data['color']
            )
            ProductPictures.objects.create(
                product_id=product,
                picture=self.cleaned_data['images']
            )
        return product
