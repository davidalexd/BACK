from .logenum import LogEnumCategoryFormatos, LogEnumFormatos,OrganizacionLog
from .models import ReportsCategoryModel, ReportsFormatsModel, User_Reportes_Categoria_Model, User_Reportes_Formatos_Model
from .serializers import FormatosReportesSerializer,CategoriaReportesSerializer
from authentication.mixins import StaffEditorPermissionMixin
from rest_framework import generics

class FormatosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = FormatosReportesSerializer    
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumFormatos.FORMATO_CREATED,User_Reportes_Formatos_Model)
formatos_create_view = FormatosListaCreateApiView.as_view()



class CategoriasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CategoriaReportesSerializer    
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumCategoryFormatos.CATEGORY_FORMATO_CREATED,User_Reportes_Categoria_Model)
categorias_create_view = CategoriasListaCreateApiView.as_view()
