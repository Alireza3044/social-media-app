from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator
from django import forms


class RegisterForm(auth_forms.UserCreationForm):
    template_name = "accounts/form_snippet.html"
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class UserEditForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        error_messages={"unique": "A user with that username already exists."},
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput({
            "class": "px-2 py-1 w-full bg-gray-100 border-2 border-gray-400 rounded-lg shadow focus:outline-blue-500",
            "placeholder": "Username...",
        }),
        label="Username:",
        validators=[UnicodeUsernameValidator]
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput({
            "id": "image-input",
            "class": "hidden",
            "accept": "image/*",
            "x-ref": "imageInput",
            "@change": "fileChosen($event)",
        }),
        label="Image:"
    )
    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput({
            "class": "px-2 py-1 w-full bg-gray-100 border-2 border-gray-400 rounded-lg shadow focus:outline-blue-500",
            "placeholder": "First name...",
        }),
        label="First name:"
    )
    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput({
            "class": "px-2 py-1 w-full bg-gray-100 border-2 border-gray-400 rounded-lg shadow focus:outline-blue-500",
            "placeholder": "Last name...",
        }),
        label="Last name:"
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput({
            "class": "px-2 py-1 w-full bg-gray-100 border-2 border-gray-400 rounded-lg shadow focus:outline-blue-500",
            "placeholder": "Email...",
        }),
        label="Email:"
    )
    
    def save(self, user: User):
        user.username = self.cleaned_data.get("username")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")
        user.save()
        
        if self.cleaned_data.get("image"):
            user.profile.image = self.cleaned_data.get("image")
            user.profile.save()
        
        return user


class LoginForm(auth_forms.AuthenticationForm):
    template_name = "accounts/form_snippet.html"


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    template_name = "accounts/form_snippet.html"


class PasswordResetForm(auth_forms.PasswordResetForm):
    template_name = "accounts/form_snippet.html"


class PasswordResetConfirmForm(auth_forms.SetPasswordForm):
    template_name = "accounts/form_snippet.html"
