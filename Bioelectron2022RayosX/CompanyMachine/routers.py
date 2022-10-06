from rest_framework.routers import DefaultRouter
from .viewsets import CalibracionesGenericViewSet, CalibracionesHistoryGenericViewSet, MedidoresGenericViewSet, MedidoresHistoryGenericViewSet

router = DefaultRouter() 
router.register('Calibraciones',CalibracionesGenericViewSet,basename='calibraciones')
router.register('Medidores',MedidoresGenericViewSet,basename='medidores')
router.register('CalibracionesHistory',CalibracionesHistoryGenericViewSet,basename='calibraciones-history')
router.register('MedidoresHistory',MedidoresHistoryGenericViewSet,basename='medidores-history')

urlpatterns = router.urls