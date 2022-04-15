from django.urls import path

from Exam_Django.staff_app import views
urlpatterns = (
    path('create_product', views.create_product_view, name='create_product'),
    path('edit_product/<str:pk>/', views.edit_item, name='edit_product'),
    path('product/delete/<str:pk>/', views.delete_item, name='delete_product'),
)
