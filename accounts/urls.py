from django.urls import path
from django.contrib.auth.views import LoginView, PasswordChangeView
from . import views, forms

app_name = "accounts"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(
        template_name="accounts/login.html",
        form_class=forms.LoginForm
        ), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password-change/", PasswordChangeView.as_view(
        template_name="accounts/password_change.html",
        form_class=forms.PasswordChangeForm
        ), name="password-change"),
    path("password-change/done/", PasswordChangeView.as_view(
        template_name="accounts/password_change.html",
        form_class=forms.PasswordChangeForm
        ), name="password-change"),
]
