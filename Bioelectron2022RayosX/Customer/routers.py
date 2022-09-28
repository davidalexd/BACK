from rest_framework.routers import DefaultRouter
from .viewsets import OrganizacionesGenericViewSet

router = DefaultRouter() 
router.register('Organizaciones',OrganizacionesGenericViewSet,basename='organizaciones')

urlpatterns = router.urls