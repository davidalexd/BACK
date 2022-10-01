from rest_framework.routers import DefaultRouter
from .viewsets import AreasHistoryGenericViewSet, DepartamentosGenericViewSet, DepartamentosHistoryGenericViewSet, OrganizacionHistoryGenericViewSet, OrganizacionesGenericViewSet,AreasGenericViewSet

router = DefaultRouter() 
router.register('Organizaciones',OrganizacionesGenericViewSet,basename='organizaciones')
router.register('Departamentos',DepartamentosGenericViewSet,basename='departamentos')
router.register('Areas',AreasGenericViewSet,basename='areas')
router.register('AreasHistory',AreasHistoryGenericViewSet,basename='areas-history')
router.register('DepartamentosHistory',DepartamentosHistoryGenericViewSet,basename='departamentos-history')
router.register('OrganizacionesHistory',OrganizacionHistoryGenericViewSet,basename='organizaciones-history')

urlpatterns = router.urls