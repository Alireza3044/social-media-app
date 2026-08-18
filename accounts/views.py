from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, views
from django.views.generic import TemplateView
from . import forms


class IndexView(TemplateView):
    template_name = "accounts/index.html"


def register_view(request):
    form = forms.RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account has been created successfuly.")
            return redirect("accounts:login")

    return render(request, "accounts/register.html", { "form": form })


class LoginView(views.LoginView):
    template_name = "accounts/login.html"
    form_class = forms.LoginForm


def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")


class PasswordChangeView(views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    form_class = forms.PasswordChangeForm
    success_url = reverse_lazy("accounts:password-change-done")


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "accounts/password_reset.html"
    form_class = forms.PasswordResetForm
    success_url = reverse_lazy("accounts:password-reset-done")
