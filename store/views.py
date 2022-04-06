from django.shortcuts import render
from django.views import generic as views

from store.Forms.product_main_form import ProductMainForm
from store.models import ProductCategory, ProductSizes, ProductGender, ProductColors, Product, ProductPictures


class StoreMainPageView(views.ListView):
    context_object_name = 'data'

    template_name = 'store/store.html'

    def get_queryset(self):
        dataset = {
            'products': Product.objects.all(),
            'picture': ProductPictures.objects.all(),
        }
        return dataset


class ProductDetailsView(views.DetailView):
    context_object_name = 'product_data'
    template_name = 'store/Product_details.html'
    model = Product

    def get_context_data(self, **kwargs):
        product = self.object
        sizes = self.object.size.all()
        colors = self.object.color.all()
        category = self.object.category.first()
        gender = self.object.gender.first()
        pictures = self.object.pictures.all()
        dataset = {
            'product':product,
            'sizes': sizes,
            'colors': colors,
            'category':category,
            'gender' : gender,
            'pictures': pictures,
            'range' : range(pictures.count()),
        }
        return dataset


# def product_details_page(request, pk):
#     product = Product.objects.get(product_id=pk)
#     sizes = product.size.all()
#     colors = product.color.all()
#     category = product.category.first()
#     gender = product.gender.first()
#
#     context = {
#         'product': product,
#         'sizes': sizes,
#         'colors': colors,
#         'category': category,
#         'gender': gender
#     }
#     return render(request, 'store/Product_details.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


# def create_product(request):
#     form = ProductMainForm()
#     if request.method.lower() == 'post':
#         form = ProductMainForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#     context = {
#         'form': form,
#     }
#     return render(request, 'store/forms/ceate_product.html', context)
#

class CreateProduct(views.CreateView):
    template_name = 'store/forms/ceate_product.html'
    form_class = ProductMainForm
    success_url = '#'


def an(requst):
    products = Product.objects.all()
    size = products.prefetch_related('productsizes_set')
    return render(requst, 'store/forms/../templates/store/some.html', {'products': products, 'size': size})
