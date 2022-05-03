from django.shortcuts import render, redirect, get_object_or_404
import cloudinary.uploader
import cloudinary
from Exam_Django.staff_app.Forms.product_main_form import ProductMainForm, EditProductForm
from Exam_Django.staff_app.decorators import check_user_group_dec
from Exam_Django.store.models import Product, ProductPictures


@check_user_group_dec('managers', 'admin')
def create_product_view(request):
    template_name = 'store/forms/create_product.html'
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
    initials = {
                'image0': '',
                'image1': '',
                'image2': '', }
    for image in range(item.pictures.all().count()):
        initials[f'image{image}'] = item.pictures.all()[image].picture.url

    form = EditProductForm(instance=item,
                           initial=initials, product=item, request=request)
    if request.method.lower() == 'post':
        form = EditProductForm(request.POST, request.FILES, product=item, instance=item, request=request)
        if form.is_valid():
            form.save()
            for imag in range(5):
                if item.pictures.all().count() > imag:
                    img = item.pictures.all()[imag]
                    if f'image{imag}' in request.FILES.keys():
                        img.picture = cloudinary.uploader.destroy(img.picture.public_id, invalidate=True)
                        img.picture = cloudinary.uploader.upload_image(
                            request.FILES[f'image{imag}'].file,
                            transformation={'width': '480',
                                            'height': '640',
                                            'aspect-ratio': '1.1',
                                            'radius': '20'},
                            folder=f'e-com/products/',
                            format='webp', )
                        img.save()
                else:
                    if f'image{imag}' in request.FILES.keys():
                        ProductPictures.objects.create(
                            product_id=item,
                            picture=cloudinary.uploader.upload_image(
                                request.FILES[f'image{imag}'].file,
                                transformation={'width': '480',
                                                'height': '640',
                                                'aspect-ratio': '1.1',
                                                'radius': '20'},
                                folder=f'e-com/products/',
                                format='webp', )
                        )
            return redirect('store')
        form = EditProductForm(request.POST, request.FILES, product=item)
    return render(request, 'store/forms/edit_product.html', {'form': form})


@check_user_group_dec('managers', 'admin')
def delete_item(request, pk):
    item = get_object_or_404(Product, product_id=pk)
    for pic in item.pictures.all():
        cloudinary.uploader.destroy(pic.picture.public_id, invalidate=True)
    item.delete()
    return redirect('store')
