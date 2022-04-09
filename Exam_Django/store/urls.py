from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Exam_Django.store import views

urlpatterns = [
    path('', views.StoreMainPageView.as_view(), name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('create_product', views.CreateProduct.as_view(), name='create_product'),
    path('product_details/<str:pk>/', views.ProductDetailsView.as_view(), name='product_details'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
