from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets.cv import CVViewset, ProjectsViewset, TechnologyViewset


app_name = "api"


router = DefaultRouter()


router.register(prefix="cv", viewset=CVViewset, basename="cv")

router.register(prefix="project", viewset=ProjectsViewset, basename="project")

router.register(prefix="technology", viewset=TechnologyViewset, basename="technology")


urlpatterns = router.urls
