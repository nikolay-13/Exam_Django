
from django.urls import path
from Exam_Django.accounts import views

urlpatterns = (
    path('registration/', views.SignUp.as_view(), name='registration'),
    path('login/', views.LogInView.as_view(), name='login_page'),
    path('logout', views.LogOut.as_view(), name='logout'),
)
