from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets.cv import CVViewset


app_name = "api"


router = DefaultRouter()


router.register(
    prefix="cv",
    viewset=CVViewset,
    basename="cv"
)


urlpatterns = router.urls
