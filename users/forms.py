from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class SetPassForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="New Password"
    )