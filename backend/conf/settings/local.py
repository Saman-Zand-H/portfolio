from .base import *


SECRET_KEY = "django-insecure-knb8h8w!zv%4=4kff2h60)n=-%e(c6sn4j_@s$@cbo2-ee(0u#"

DEBUG = True


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'postgres',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": env.str("DB_HOST", "localhost"),
        "PORT": 5432,
    }
}
