from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="mdeditor/", view=include("mdeditor.urls")),
    path(route="api/v1/", view=include("api.urls", namespace="api")),
    path(route="graphql/v1/", view=include("gql.urls")),
    path(route="", view=include("blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
