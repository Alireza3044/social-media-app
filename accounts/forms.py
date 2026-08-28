from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterForm(auth_forms.UserCreationForm):
    template_name = "accounts/form_snippet.html"
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UserEditForm(forms.ModelForm):
    template_name = "accounts/form_snippet.html"
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


class LoginForm(auth_forms.AuthenticationForm):
    template_name = "accounts/form_snippet.html"


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    template_name = "accounts/form_snippet.html"


class PasswordResetForm(auth_forms.PasswordResetForm):
    template_name = "accounts/form_snippet.html"


class PasswordResetConfirmForm(auth_forms.SetPasswordForm):
    template_name = "accounts/form_snippet.html"
