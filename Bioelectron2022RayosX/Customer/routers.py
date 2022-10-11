from rest_framework.routers import DefaultRouter
from .viewsets import ContactosGenericViewSet,DepartamentosGenericViewSet, OrganizacionesGenericViewSet,AreasGenericViewSet

router = DefaultRouter() 
router.register('Organizaciones',OrganizacionesGenericViewSet,basename='organizaciones')
router.register('Departamentos',DepartamentosGenericViewSet,basename='departamentos')
router.register('Areas',AreasGenericViewSet,basename='areas')
router.register('Contactos',ContactosGenericViewSet,basename='contactos')

urlpatterns = router.urls