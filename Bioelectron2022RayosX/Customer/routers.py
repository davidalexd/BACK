from rest_framework.routers import DefaultRouter
from .viewsets import ContactosGenericViewSet,DepartamentosGenericViewSet, OrganizacionesGenericViewSet,AreasGenericViewSet

router = DefaultRouter() 
router.register('Organizaciones',OrganizacionesGenericViewSet,basename='organizaciones')
router.register('Departamentos',DepartamentosGenericViewSet,basename='departamentos')
router.register('Areas',AreasGenericViewSet,basename='areas')
router.register('Contactos',ContactosGenericViewSet,basename='contactos')
# router.register('AreasHistory',AreasHistoryGenericViewSet,basename='areas-history')
# router.register('DepartamentosHistory',DepartamentosHistoryGenericViewSet,basename='departamentos-history')
# router.register('OrganizacionesHistory',OrganizacionHistoryGenericViewSet,basename='organizaciones-history')
# router.register('ContactosHistory',ContactosHistoryGenericViewSet,basename='contactos-history')

urlpatterns = router.urls