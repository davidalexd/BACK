from .logenum import LogEnumFormatos,OrganizacionLog,LogEnumCategoryFormatos
from rest_framework import mixins,viewsets,mixins
from .models import ReportsCategoryModel, ReportsFormatsModel, User_Reportes_Categoria_Model, User_Reportes_Formatos_Model
from .serializers import CategoriaReportesSerializer, FormatosReportesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class FormatosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = FormatosReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumFormatos.FORMATO_CREATED,User_Reportes_Formatos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumFormatos.FORMATO_UPDATED,User_Reportes_Formatos_Model)

class CategoriasFormatosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = CategoriaReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumCategoryFormatos.CATEGORY_FORMATO_CREATED,User_Reportes_Categoria_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumCategoryFormatos.CATEGORY_FORMATO_UPDATED,User_Reportes_Categoria_Model)
