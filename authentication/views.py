from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.views import View
from authentication.forms import RegisterUserForm, LoginUserForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        form.save(commit=False)
        user_email = form.cleaned_data['email']
        user_username = form.cleaned_data['username']
        user_password = form.cleaned_data['password1']

        # Create new user
        user = User.objects.create_user(username=user_username, email=user_email, password=user_password)

        user.is_active = False
        send_email(user)

        return redirect('authentication:login')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('core:home')


def privacy(request):
    return render(request, 'auth/privacy.html', {'title': 'Privacy policy and terms of use'})


def logout_user(request):
    logout(request)
    return redirect('authentication:login')
