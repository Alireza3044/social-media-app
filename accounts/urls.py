from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password-change/", views.PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done/", views.PasswordChangeDoneView.as_view(), name="password-change-done"),
]
