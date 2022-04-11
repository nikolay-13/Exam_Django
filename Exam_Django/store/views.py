from django.db.models import Q
from django.shortcuts import render
from django.views import generic as views

from Exam_Django.store.Forms.product_main_form import ProductMainForm
from Exam_Django.store.models import Product


class StoreMainPageView(views.ListView):
    context_object_name = 'data'

    template_name = 'store/Store.html'

    def get_queryset(self):
        q = self.request.GET.get('q') if self.request.GET.get('q') else ''
        current_cat = q.lower()
        if not q == '':
            gender, category = q.split('/')
        else:
            category, gender = '', ''
        products = Product.objects.filter(
            Q(gender__gender__icontains=gender.lower()) &
            Q(category__category__icontains=category.lower())
        )
        if current_cat == '':
            current_cat = 'All Items'
        dataset = {
            'products': products,
            'category': current_cat,
        }
        print(self.request.user)
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
            'product': product,
            'sizes': sizes,
            'colors': colors,
            'category': category,
            'gender': gender,
            'pictures': pictures,
            'range': range(pictures.count()),
        }
        return dataset


def cart(request):
    context = {}
    return render(request, 'store/Cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/Checkout.html', context)


class CreateProduct(views.CreateView):
    template_name = 'store/forms/ceate_product.html'
    form_class = ProductMainForm
    success_url = '#'

