from rest_framework.viewsets import ReadOnlyModelViewSet

from cv.models import CV, Project, Technology
from api.serializers.cv import CVSerializer, ProjectSerializer, TechnologySerializer


class CVViewset(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class ProjectsViewset(ReadOnlyModelViewSet):
    queryset = Project.objects.prefetch_related("technologies", "images").all()
    serializer_class = ProjectSerializer


class TechnologyViewset(ReadOnlyModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
