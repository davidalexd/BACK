from rest_framework.routers import DefaultRouter
from .viewsets import FormatosGenericViewSet,CategoriasFormatosGenericViewSet

router = DefaultRouter() 
router.register('Formats',FormatosGenericViewSet,basename='formatos')
router.register('CategoryFormats',CategoriasFormatosGenericViewSet,basename='categorias-formatos')

urlpatterns = router.urls