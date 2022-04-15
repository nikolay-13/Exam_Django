from django.shortcuts import render, redirect, get_object_or_404

from Exam_Django.staff_app.Forms.product_main_form import ProductMainForm, EditProductForm
from Exam_Django.staff_app.decorators import check_user_group_dec
from Exam_Django.store.models import Product


@check_user_group_dec('managers', 'admin')
def create_product_view(request):
    template_name = 'store/forms/ceate_product.html'
    form = ProductMainForm()
    if request.method.lower() == 'post':
        form = ProductMainForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save(commit=True)
            return redirect('store')
        form = ProductMainForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@check_user_group_dec('managers', 'admin')
def edit_item(request, pk):
    item = Product.objects.get(product_id=pk)
    form = EditProductForm(instance=item,
                           initial={
                               'category': item.category.first(),
                               'size': item.size.first(),
                               'gender': item.gender.first(),
                               'color': item.color.first(),
                           }, product=item, request=request)
    if request.method.lower() == 'post':
        form = EditProductForm(request.POST, request.FILES, product=item, instance=item, request=request)
        if form.is_valid():
            form.save()
            return redirect('store')
        form = EditProductForm(request.POST, request.FILES, product=item)
    return render(request, 'store/forms/edit_product.html', {'form': form})


@check_user_group_dec('managers', 'admin')
def delete_item(request, pk):
    item = get_object_or_404(Product,product_id=pk)
    item.delete()
    return redirect('store')
