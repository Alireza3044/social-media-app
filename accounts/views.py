from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views
from django.views.generic import TemplateView, FormView
from . import forms


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"


class ProfileEditView(FormView):
    form_class = forms.ProfileEditForm
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_initial(self):
        initial = super().get_initial()
        user = self.request.user
        initial.update({
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "image": user.profile.image
        })
        return initial
    
    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


class RegisterView(FormView):
    form_class = forms.RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        messages.success(self.request, f"Welcome {username}, your account has been created successfuly.")
        return super().form_valid(form)


class LoginView(views.LoginView):
    template_name = "accounts/login.html"


class LogoutView(views.LogoutView):
    template_name = "accounts/logout.html"


class PasswordChangeView(views.PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("accounts:password-change-done")


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "accounts/password_change_done.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "accounts/password_reset.html"
    success_url = reverse_lazy("accounts:password-reset-done")
    email_template_name = "accounts/password_reset_email.html"


class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password-reset-complete")


class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"
