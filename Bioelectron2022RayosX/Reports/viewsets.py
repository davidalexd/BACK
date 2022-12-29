from rest_framework.exceptions import APIException,status
from rest_framework.response import Response
from rest_framework import mixins,viewsets,mixins
from .models import ReportsCategoryModel, ReportsFormatsModel, ReportsReporteModel
from .serializers import CategoriaReportesSerializer, FormatosReportesSerializer, ReporteReportesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class FormatosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = FormatosReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class CategoriasFormatosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = CategoriaReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class ReportesFormatosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = ReporteReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

        
class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No se encontraron registros', })

