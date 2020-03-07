from rest_framework import viewsets, views
from . import models
from . import serializers


class TareasuViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.TareasuSerializer

class TareaseViewSet(viewsets.ModelViewSet):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.TareaseSerializer

class TareastViewSet(viewsets.ModelViewSet):
    queryset = models.Tarea.objects.all()
    serializer_class = serializers.TareastSerializer    