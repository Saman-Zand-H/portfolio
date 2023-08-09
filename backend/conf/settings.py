"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os, sys
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, 'apps'))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', "django-insecure-knb8h8w!zv%4=4kff2h60)n=-%e(c6sn4j_@s$@cbo2-ee(0u#")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', 0)

ALLOWED_HOSTS = [
    "backend",
    "172.17.0.1",
    "localhost",
    "whiteelli.tk",
    "samanznd.ir",
    "backend.samanznd.ir",
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
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'allauth',
    'allauth.account',
    'django_filters',
    'corsheaders',
    'mdeditor',
    'graphene_django',
    'rest_framework',
    
    'users.apps.UsersConfig',
    'cv',
    'blog',
    'api',
    'gql'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"    
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DB_NAME', 'postgres'),
        'USER': env.str('DB_USER', 'postgres'),
        'PASSWORD': env.str('DB_PASSWORD', 'postgres'),
        'HOST': env.str('DB_HOST', 'db'),
        'PORT': env.int('DB_PORT', 5432)
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.UserModel'

# Production Configurations
if env.str("ENVIRONMENT", 'production') == 'production':
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
    
    SECURE_HSTS_SECONDS = env.int('HSTS_AGE', 3600)
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATIFILES_DIRS = [BASE_DIR / "static"]

MEDIA_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = "/media/"
MEDIA_ROOT = "media"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# MDEditor configuration
MDEDITOR_CONFIGS = {
    'default': {
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"], 
        'upload_image_formats': ["jpg", "jpeg", "gif", "png","svg"],
        'image_folder': 'editor',
        'theme': 'default', 
        'preview_theme': 'default',
        'editor_theme': 'pastel-on-dark', 
        'toolbar_autofixed': False, 
        'search_replace': True,
        'emoji': True, 
        'tex': True, 
        'flow_chart': True, 
        'sequence': True, 
        'watch': True,
        'lineWrapping': True, 
        'lineNumbers': True, 
        'language': 'en'
    }
}

