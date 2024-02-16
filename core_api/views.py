from rest_framework import viewsets
from rest_framework import permissions
from core.models import Alumno
from core_api import serializers


# Create your views here.
class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all().order_by('id')
    serializer_class = serializers.AlumnoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]