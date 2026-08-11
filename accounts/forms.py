from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    template_name = "accounts/form_snippet.html"


class RegisterForm(UserCreationForm):
    template_name = "accounts/form_snippet.html"
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
