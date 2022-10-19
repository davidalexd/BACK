from rest_framework.routers import DefaultRouter

from .viewsets import CategoriaOperacionesGenericViewSet, OperacionesGenericViewSet, VariableGenericViewSet

router = DefaultRouter() 
router.register('Operaciones',OperacionesGenericViewSet,basename='operaciones')
router.register('Variables',VariableGenericViewSet,basename='variables')
router.register('CategoriaOperaciones',CategoriaOperacionesGenericViewSet,basename='categoria-operaciones')
urlpatterns = router.urls