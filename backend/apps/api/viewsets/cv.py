from rest_framework.viewsets import ReadOnlyModelViewSet

from cv.models import CV, Project
from api.serializers.cv import CVSerializer, ProjectSerializer


class CVViewset(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    
    
class ProjectsViewset(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    