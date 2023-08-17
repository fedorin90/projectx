from django import forms

from core.models import NewsletterSub


class ContactForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control"}))
    last_name = forms.CharField(label='Last name', max_length=50, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control"}))
    email = forms.EmailField(label='Email', max_length=150, widget=forms.EmailInput(attrs={
        'type': "email", 'class': "form-control"}))
    message = forms.CharField(label='Message', max_length=2000, widget=forms.Textarea(attrs={
        'cols': '30', 'rows': '5', 'class': "form-control"}))
    # captcha = CaptchaField()


class OrderByForm(forms.Form):
    order_by = forms.ChoiceField(label="Sort by", choices=('name', 'create', 'update'))


class NewsletterSubForm(forms.Form):
    model = NewsletterSub
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={
        'type': "text", 'class': "form-control"}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(attrs={
        'type': "email", 'class': "form-control"}))
