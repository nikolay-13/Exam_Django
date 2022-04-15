from django.urls import path
from Exam_Django.cart import views

urlpatterns = (
    path('store/cart/', views.cart_details, name='cart_details'),
    path('store/cart/add/<str:product_pk>/', views.add_to_cart, name='add_to_cart'),
    path('store/cart/remove/<str:product_pk>/', views.remove_from_cart, name='remove_from_cart'),


)
