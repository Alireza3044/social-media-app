from django.shortcuts import redirect
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)


class AuthenticationMiddleware:
    """Requires authentication for all pages except public endpoints."""

    def __init__(self, get_response):
        self.get_response = get_response
        
        self.index_url = reverse("accounts:index")
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:login")
        self.logout_url = reverse("accounts:logout")
        
        # Public URLs that don't require authentication
        self.public_urls = [
            self.register_url,
            self.login_url,
            reverse("accounts:password-reset"),
            "/admin/",
        ]
    
    def __call__(self, request):
        """Handle request: allow if authenticated or on public URL, otherwise redirect to login."""
        logger.debug(f"Processing request: {request.method} {request.path}")

        # Redirect authenticated users away from login/register
        if request.user.is_authenticated:
            if request.path.startswith(self.register_url) or request.path.startswith(self.login_url):
                logger.debug(f"Authenticated user redirected from auth page: {request.path}")
                
                return redirect(self.index_url)
            return self.get_response(request)
        
        # Unauthenticated users
        else:
            if request.path.startswith(self.logout_url):
                logger.debug(f"Unauthenticated user redirected from logout: {request.path}")
                return redirect(self.login_url)
            
            # Allow unauthenticated access to public pages
            for url in self.public_urls:
                if request.path.startswith(url):
                    logger.debug(f"Public URL access allowed: {request.path}")
                    return self.get_response(request)
            
            # Redirect to login for protected pages
            logger.info(f"Redirecting unauthenticated user to login: {request.path}")
            return redirect(self.login_url)
