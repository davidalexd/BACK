from rest_framework.routers import DefaultRouter
from .viewsets import ProtocolosGenericViewSet, PruebasCalculoGenericViewSet, PruebasOpcionGenericViewSet, SeccionesGenericViewSet, VariableGenericViewSet

router = DefaultRouter() 
router.register('Protocolos',ProtocolosGenericViewSet,basename='protocolos')
router.register('Secciones',SeccionesGenericViewSet,basename='secciones')
router.register('PruebasCalculo',PruebasCalculoGenericViewSet,basename='pruebas-calculo')
router.register('PruebasOpciones',PruebasOpcionGenericViewSet,basename='pruebas-opciones')
router.register('Variables',VariableGenericViewSet,basename='variables')

urlpatterns = router.urls