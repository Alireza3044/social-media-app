from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, views
from django.views.generic import TemplateView
from django.templatetags.static import static
from . import forms, models


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"


def profile_edit_view(request):
    user_form = forms.UserEditForm(instance=request.user)
    profile_form = forms.ProfileEditForm(instance=request.user.profile)
    
    if request.method == "POST":
        user_form = forms.UserEditForm(request.POST, instance=request.user)
        profile_form = forms.ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("accounts:profile")
    
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "header": "Edit Profile",
        "btn_text": "Submit",
    }
    return render(request, "accounts/profile_edit.html", context)


def register_view(request):
    form = forms.RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            models.Profile.objects.create(user=user)
            
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account has been created successfuly.")
            return redirect("accounts:login")

    context = {
        "form": form,
        "header": "Register",
        "btn_text": "Register",
    }
    return render(request, "accounts/box_form.html", context)


class LoginView(views.LoginView):
    template_name = "accounts/login.html"
    form_class = forms.LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Login"
        context["btn_text"] = "Login"
        return context


def logout_view(request):
    logout(request)

    context = {
        "header": "You have been logged out.",
        "btn_text": "Go to Login",
        "path_name": "accounts:login"
    }
    return render(request, "accounts/box_message.html", context=context)


class PasswordChangeView(views.PasswordChangeView):
    template_name = "accounts/box_form.html"
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy("accounts:password-change-done")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Password Change"
        context["btn_text"] = "Change"
        return context


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "accounts/box_message.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["header"] = "Your Password has been changed"
            context["btn_text"] = "Go to Index"
            context["path_name"] = "accounts:profile"
            return context

class PasswordResetView(views.PasswordResetView):
    template_name = "accounts/box_form.html"
    form_class = forms.PasswordResetForm
    success_url = reverse_lazy("accounts:password-reset-done")
    email_template_name = "accounts/password_reset_email.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Password Reset"
        context["btn_text"] = "Submit"
        context["message"] = "Please enter your email. We would send you an email consisting the link for resetting your password."
        return context


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "accounts/box_message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Your email has been sent"
        context["message"] = "Check your inbox for the password reset link."
        return context


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "accounts/box_form.html"
    form_class = forms.PasswordResetConfirmForm
    success_url = reverse_lazy("accounts:password-reset-complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Password Reset"
        context["btn_text"] = "Reset"
        return context


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "accounts/box_message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Password Reset"
        context["btn_text"] = "Go to Login"
        context["path_name"] = "accounts:login"
        return context
