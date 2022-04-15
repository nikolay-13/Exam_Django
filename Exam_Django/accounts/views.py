from django import views
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordResetView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from Exam_Django.accounts.forms.user_profile_form import UserProfileCreationForm, UserLogInForm, EditProfileForm
from Exam_Django.accounts.models.models import Profile

UserModel = get_user_model()


class SignUp(views.generic.edit.FormView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('store')
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        user = form.save(commit=True)
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super(SignUp, self).form_invalid(form)


class LogInView(views.generic.View):
    template_name = 'accounts/login.html'
    form_class = UserLogInForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.login(request.POST)
            if user:
                login(request, user)
                return redirect('store')
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


class LogOut(LogoutView):
    next_page = reverse_lazy('login_page')


class ProfileDetailsView(views.generic.View):
    template_name = 'accounts/profile_page.html'

    def get(self, request):
        user = get_user(request)
        if user:
            context = {
                'profile': user,
                'picture': user.profile_picture,
            }
            return render(request, self.template_name, context)
        return HttpResponse('<h1>Unauthorized</h1>', status=401)


class EditProfileView(views.generic.View):
    template_name = 'accounts/edit_profile.html'
    form_class = EditProfileForm

    def get(self, request):
        user = get_user(request)
        if user:
            context = {
                'form': self.form_class(
                    initial={
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'tel_number': user.tel_number,
                        'profile_picture': user.profile_picture,
                        'email': user.user.email,
                    }),
                'pic': user.profile_picture,
            }
            return render(request, self.template_name, context)
        return HttpResponse('<h1>Unauthorized</h1>', status=401)

    def post(self, request):
        user = get_user(request)
        if user:
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.tel_number = form.cleaned_data['tel_number']
                user.profile_picture = form.cleaned_data['profile_picture'] or user.profile_picture
                user.user.email = form.cleaned_data['email']
                user.save()
                return redirect('profile_page')
            return render(request, self.template_name, {'form': form})
        return HttpResponse('<h1>Unauthorized</h1>', status=401)


class DeleteProfileView(views.generic.View):
    template_name = 'accounts/delete.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = get_user(request)
        if user:
            user.user.delete()
            return redirect('login_page')
        return HttpResponse('<h1>Unauthorized</h1>', status=401)


def get_user(request):
    if not request.user == 'AnonymousUser':
        if request.user.is_authenticated:
            user = get_object_or_404(Profile, user=request.user)
            if request.user == user.user:
                return user
    return None


class PasswordChange(PasswordChangeView):
    template_name = 'accounts/password/change_password.html'
    success_url = reverse_lazy('logout_c')


class ResetPassword(PasswordResetView):
    template_name = 'accounts/password/reset_password.html'
    success_url = reverse_lazy('logout_c')
