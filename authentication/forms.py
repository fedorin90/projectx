
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'type': "text", 'class': "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control"}))
    checkbox = forms.BooleanField(label='privacy policy and terms of use', required=True, widget=forms.CheckboxInput(
        attrs={'type': "checkbox"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'checkbox')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login or email', widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'type': "password", 'class': "form-control"}))




# class OAuthSingUpForm(BaseSignupForm):
#     username = forms.CharField(
#         label=_("Username"),
#         min_length=app_settings.USERNAME_MIN_LENGTH,
#         widget=forms.TextInput(
#             attrs={"placeholder": _("Username"), "autocomplete": "username", 'type': "text", 'class': "form-control"}
#         ),
#     )
#     email = forms.EmailField(
#         widget=forms.TextInput(
#             attrs={
#                 "type": "email",
#                 "placeholder": _("E-mail address"),
#                 "autocomplete": "email",
#                 'class': "form-control"
#             }
#         )
#     )
