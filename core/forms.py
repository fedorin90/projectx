from django import forms


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
