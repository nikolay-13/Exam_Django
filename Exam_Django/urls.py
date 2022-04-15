from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Exam_Django.store.urls')),
    path('accounts/', include('Exam_Django.accounts.urls')),
    path('store/manager/',include('Exam_Django.staff_app.urls')),
    path('store/cart/' ,include('Exam_Django.cart.urls')),
]
