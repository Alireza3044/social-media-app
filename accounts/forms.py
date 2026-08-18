from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django import forms


class RegisterForm(auth_forms.UserCreationForm):
    template_name = "accounts/form_snippet.html"
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(auth_forms.AuthenticationForm):
    template_name = "accounts/form_snippet.html"


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    template_name="accounts/form_snippet.html"


class PasswordResetForm(auth_forms.PasswordResetForm):
    template_name="accounts/form_snippet.html"
