from django.urls import path
from django.contrib.auth.views import LoginView
from . import views, forms

app_name = "accounts"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", LoginView.as_view(
        template_name="accounts/login.html", authentication_form=forms.LoginForm
        ), name="login"),
    path("logout/", views.logout_view, name="logout"),
]
