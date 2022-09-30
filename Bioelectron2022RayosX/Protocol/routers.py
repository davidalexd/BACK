from rest_framework.routers import DefaultRouter
from .viewsets import ProtocoloHistoryGenericViewSet, ProtocolosGenericViewSet, PruebaCalculoHistoryGenericViewSet, PruebaOpcionHistoryGenericViewSet, PruebasCalculoGenericViewSet, PruebasOpcionGenericViewSet, SeccionesGenericViewSet, SeccionesHistoryGenericViewSet, VariableGenericViewSet, VariablesHistoryGenericViewSet

router = DefaultRouter() 
router.register('Protocolos',ProtocolosGenericViewSet,basename='protocolos')
router.register('Secciones',SeccionesGenericViewSet,basename='secciones')
router.register('PruebasCalculo',PruebasCalculoGenericViewSet,basename='pruebas-calculo')
router.register('PruebasOpciones',PruebasOpcionGenericViewSet,basename='pruebas-opciones')
router.register('Variables',VariableGenericViewSet,basename='variables')

router.register('ProtocolosHistory',ProtocoloHistoryGenericViewSet,basename='protocolos-history')
router.register('SeccionesHistory',SeccionesHistoryGenericViewSet,basename='secciones-history')
router.register('PruebasCalculoHistory',PruebaCalculoHistoryGenericViewSet,basename='prueba-calculo-history')
router.register('PruebasOpcionesHistory',PruebaOpcionHistoryGenericViewSet,basename='prueba-opciones-history')
router.register('VariablesHistory',VariablesHistoryGenericViewSet,basename='variables-history')

urlpatterns = router.urls