from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from store import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.StoreMainPageView.as_view(), name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('create_product', views.CreateProduct.as_view(), name='create_product'),
    path('none/', views.an, ),
    path('product_details/<str:pk>/',views.ProductDetailsView.as_view(), name='product_details' ),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
