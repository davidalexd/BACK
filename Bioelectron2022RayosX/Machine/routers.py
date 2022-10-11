from rest_framework.routers import DefaultRouter
from .viewsets import SistemasGenericViewSet, TubosGenericViewSet

router = DefaultRouter() 
router.register('Sistemas',SistemasGenericViewSet,basename='sistemas')
router.register('Tubos',TubosGenericViewSet,basename='tubos')
# router.register('SistemasHistory',SistemasHistoryGenericViewSet,basename='sistemas-history')
# router.register('TubosHistory',TubosHistoryGenericViewSet,basename='tubos-history')

urlpatterns = router.urls