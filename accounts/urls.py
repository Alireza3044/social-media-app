from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
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
        form_class=forms.PasswordChangeForm,
        success_url=reverse_lazy("accounts:password-change-done")
        ), name="password-change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
        ), name="password-change-done"),
]
