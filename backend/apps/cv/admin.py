from django.contrib import admin

from .models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    ...