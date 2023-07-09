from allauth.account.forms import SignupForm, PasswordField, LoginForm, BaseSignupForm
from allauth.socialaccount.forms import SignupForm as SF


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': False,
            })


class MyCustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': False,
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': False,
        })
        self.fields['remember'].widget.attrs.update({
            'type': "checkbox"
        })


class MySocialSignupForm(SF):
    def __init__(self, *args, **kwargs):
        super(MySocialSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': False,
            })
