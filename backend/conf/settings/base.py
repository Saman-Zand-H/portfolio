from sentry_sdk.integrations.django import DjangoIntegration
import os, sys, sentry_sdk
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(os.path.join(BASE_DIR, "apps"))


# Quick-start development settings

ALLOWED_HOSTS = [
    "backend",
    "172.17.0.1",
    "localhost",
    "whiteelli.tk",
    "samanznd.ir",
    "backend.samanznd.ir",
    "91.107.129.206",
]

SITE_ID = 1

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "https://localhost",
    "https://frontend",
    "http://frontend",
    "https://whiteelli.tk",
    "http://whiteelli.tk",
    "http://samanznd.ir",
    "https://samanznd.ir",
    "http://backend.samanznd.ir",
    "https://backend.samanznd.ir",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "django_filters",
    "corsheaders",
    "mdeditor",
    "graphene_django",
    "rest_framework",
    "users.apps.UsersConfig",
    "cv",
    "blog",
    "api",
    "gql",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "conf.urls"

# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "conf.asgi.application"

STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"

MEDIA_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "/media/"
MEDIA_ROOT = "media"


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.UserModel"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# MDEditor configuration
MDEDITOR_CONFIGS = {
    "default": {
        "toolbar": [
            "undo",
            "redo",
            "|",
            "bold",
            "del",
            "italic",
            "quote",
            "ucwords",
            "uppercase",
            "lowercase",
            "|",
            "h1",
            "h2",
            "h3",
            "h5",
            "h6",
            "|",
            "list-ul",
            "list-ol",
            "hr",
            "|",
            "link",
            "reference-link",
            "image",
            "code",
            "preformatted-text",
            "code-block",
            "table",
            "datetime",
            "emoji",
            "html-entities",
            "pagebreak",
            "goto-line",
            "|",
            "help",
            "info",
            "||",
            "preview",
            "watch",
            "fullscreen",
        ],
        "upload_image_formats": ["jpg", "jpeg", "gif", "png", "svg"],
        "image_folder": "editor",
        "theme": "default",
        "preview_theme": "default",
        "editor_theme": "pastel-on-dark",
        "toolbar_autofixed": False,
        "search_replace": True,
        "emoji": True,
        "tex": True,
        "flow_chart": True,
        "sequence": True,
        "watch": True,
        "lineWrapping": True,
        "lineNumbers": True,
        "language": "en",
    }
}


# Sentry Configurations
SENTRY_DSN = env.str("SENTRY_DSN")
sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
    profiles_sample_rate=1.0,
)
