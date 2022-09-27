from rest_framework.routers import DefaultRouter
from .viewsets import DepartamentosGenericViewSet, OrganizacionesGenericViewSet,AreasGenericViewSet

router = DefaultRouter() 
router.register('Organizaciones',OrganizacionesGenericViewSet,basename='organizaciones')
router.register('Departamentos',DepartamentosGenericViewSet,basename='departamentos')
router.register('Areas',AreasGenericViewSet,basename='areas')

urlpatterns = router.urls