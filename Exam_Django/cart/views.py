from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from Exam_Django.cart.forms import CartAddItem
from Exam_Django.store.models import Product
from Exam_Django.cart.cart import Cart


@require_POST
def add_to_cart(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id=product_pk)
    sizes = request.POST.get('size')
    colors = request.POST.get('color')
    qnt = request.POST.get('quantity')
    form = CartAddItem(request.POST,
                       color_choice=((colors, colors),),
                       size_choice=((sizes, sizes),),
                       av_qnt=((qnt,qnt),)
                       )
    if form.is_valid():
        cl_dat = form.cleaned_data
        cart.add(product=product,
                 quantity=cl_dat['quantity'],
                 size=cl_dat['size'],
                 color=cl_dat['color'],
                 update_quantity=cl_dat['update_quantity'],
                 )
        return redirect('cart_details')


def remove_from_cart(request, product_pk):
    cart = Cart(request)
    product = get_object_or_404(Product, product_id=product_pk)
    cart.remove(product)
    return redirect('cart_details')


def cart_details(request):
    cart = Cart(request)
    template_name = 'cart/cart_details.html'
    context = {
        'cart': cart
    }
    return render(request, template_name, context)
