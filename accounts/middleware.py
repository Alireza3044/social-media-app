from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    """Requires authentication for all pages except public endpoints."""

    def __init__(self, get_response):
        self.get_response = get_response
        
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:login")
        self.logout_url = reverse("accounts:logout")
        self.password_reset_url = reverse("accounts:password-reset")
        
        self.public_urls = [
            self.register_url,
            self.login_url,
            self.password_reset_url,
            "/admin/",
        ]
        self.logged_in_excluded_urls = [
            self.register_url,
            self.login_url,
            self.password_reset_url,
        ]
    
    def __call__(self, request):
        """Handle request: allow if authenticated or on public URL, otherwise redirect to login."""

        # Authenticated
        if request.user.is_authenticated:
            for url in self.logged_in_excluded_urls:
                if request.path.startswith(url):
                    return redirect("accounts:profile")
            return self.get_response(request)
        
        # Not Authenticated
        else:
            # Allow unauthenticated access to public pages
            for url in self.public_urls:
                if request.path.startswith(url):
                    return self.get_response(request)
            
            # Redirect to login for protected pages
            return redirect(self.login_url)
