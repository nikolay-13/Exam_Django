from django import views
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Exam_Django.accounts.forms.user_profile_form import UserProfileCreationForm, UserLogInForm


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
