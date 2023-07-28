from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path(
        route='admin/', 
        view=admin.site.urls
    ),
    
    path(
        route="api/v1/",
        view=include("api.urls", namespace="api")
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
