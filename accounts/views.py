from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from . import forms


def index_view(request):
    return render(request, "accounts/index.html")


def register_view(request):
    form = forms.RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}, your account has been created successfuly.")
            return redirect("accounts:login")

    return render(request, "accounts/register.html", { "form": form })


def logout_view(request):
    logout(request)
    return render(request, "accounts/logout.html")
