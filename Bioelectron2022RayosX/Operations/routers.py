from rest_framework.routers import DefaultRouter
from .viewsets import OperacionesGenericViewSet,SistemasHistoryGenericViewSet

router = DefaultRouter() 
router.register('Operaciones',OperacionesGenericViewSet,basename='operaciones')
router.register('OperacionesHistory',SistemasHistoryGenericViewSet,basename='operaciones-history')

urlpatterns = router.urls