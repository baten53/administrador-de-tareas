from tareas.viewsets import TareasuViewSet, TareaseViewSet, TareastViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario/', TareasuViewSet)
router.register('estado/', TareaseViewSet)
router.register('tarea/', TareastViewSet)