from rest_framework.routers import DefaultRouter
from .viewsets import FormatosGenericViewSet,CategoriasFormatosGenericViewSet,ReportesFormatosGenericViewSet

router = DefaultRouter() 
router.register('Formats',FormatosGenericViewSet,basename='formatos')
router.register('CategoryFormats',CategoriasFormatosGenericViewSet,basename='categorias-formatos')
router.register('ReportFormats',ReportesFormatosGenericViewSet,basename='report-formatos')

urlpatterns = router.urls
