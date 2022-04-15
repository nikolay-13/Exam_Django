from django.urls import path
from Exam_Django.accounts import views

urlpatterns = (
    path('registration/', views.SignUp.as_view(), name='registration'),
    path('login/', views.LogInView.as_view(), name='login_page'),
    path('logout', views.LogOut.as_view(), name='logout_c'),
    path('profile/', views.ProfileDetailsView.as_view(), name='profile_page'),
    path('profile/edit/', views.EditProfileView.as_view(), name='edit_profile'),
    path('profile/delete/', views.DeleteProfileView.as_view(), name='delete_profile'),
    path('accounts/change_password/', views.PasswordChange.as_view(), name='change_password'),
    path('accounts/reset_password/', views.ResetPassword.as_view(), name='reset_password'),
)
