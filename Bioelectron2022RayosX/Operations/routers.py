from rest_framework.routers import DefaultRouter
from .viewsets import OperacionesGenericViewSet

router = DefaultRouter() 
router.register('Operaciones',OperacionesGenericViewSet,basename='operaciones')

urlpatterns = router.urls