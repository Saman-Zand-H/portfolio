from rest_framework.viewsets import ReadOnlyModelViewSet

from cv.models import CV
from api.serializers.cv import CVSerializer


class CVViewset(ReadOnlyModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
    