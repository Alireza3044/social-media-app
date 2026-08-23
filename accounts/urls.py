from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("register/", views.register_view, name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("password-change/", views.PasswordChangeView.as_view(), name="password-change"),
    path("password-change/done/", views.PasswordChangeDoneView.as_view(), name="password-change-done"),
    path("password-reset/", views.PasswordResetView.as_view(), name="password-reset"),
    path("password-reset/done/", views.PasswordResetDoneView.as_view(), name="password-reset-done"),
    path("password-reset/confirm/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path("password-reset/complete/", views.PasswordResetCompleteView.as_view(), name="password-reset-complete"),
]
