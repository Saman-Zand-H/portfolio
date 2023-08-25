from .base import *


SECRET_KEY = env.str("SECRET_KEY")

DEBUG = False


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME", "postgres"),
        "USER": env.str("DB_USER", "postgres"),
        "PASSWORD": env.str("DB_PASSWORD", "postgres"),
        "HOST": env.str("DB_HOST", "localhost"),
        "PORT": env.int("DB_PORT", 5432),
    }
}


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# todo: Content Security Policy
# CSP_DIRECTIVES = {
#     'default-src': ["'self'"],
#     'script-src': ["'self'"],
#     'style-src': ["'self'", "'unsafe-inline'"],
#     'img-src': ["'self'", "data:"],
# }
# CSP_REPORT_ONLY = True
# CSP_REPORT_URI = "/csp-report/"

SECURE_HSTS_SECONDS = env.int("HSTS_AGE", 3600)
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"