from rest_framework.exceptions import APIException,status

from .models import ReportsCategoryModel, ReportsFormatsModel,ReportsReporteModel,ReportsCertificadoModel
from .serializers import FormatosReportesSerializer,ReporteReportesOpcionesSerializer,CategoriaReportesSerializer,ReporteReportesSerializer,ReporteReportesPruebasSerializer,ReporteReportesClienteSerializer,ReporteReportesSistemaControlCalidadSerializer,ReporteReportesMaquinaControlCalidadSerializer,CertificadoReportesSerializer
from authentication.mixins import StaffEditorPermissionMixin
from rest_framework import generics
from rest_framework.response import Response

class FormatosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = FormatosReportesSerializer    
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
formatos_create_view = FormatosListaCreateApiView.as_view()

class FormatosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = FormatosReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
formatos_list_view = FormatosDetallesAPIView.as_view()

class FormatosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = FormatosReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
formatos_actualizar_view = FormatosAztualizacionAPIView.as_view()

class FormatosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = FormatosReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsFormatsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
        
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
formatos_eliminar_view = FormatosEliminarAPIView.as_view()

class CategoriasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CategoriaReportesSerializer    
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        if not queryset:
            raise ValidationError
        return ({'data':queryset, 'response': status.HTTP_404_NOT_FOUND})
    def perform_create(self, serializer):
        instance = serializer.save()
categorias_create_view = CategoriasListaCreateApiView.as_view()

class CategoriasDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = CategoriaReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
categorias_list_view = CategoriasDetallesAPIView.as_view()

class CategoriasAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = CategoriaReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
categorias_actualizar_view = CategoriasAztualizacionAPIView.as_view()

class CategoriasEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = CategoriaReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsCategoryModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
        
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
categorias_eliminar_view = CategoriasEliminarAPIView.as_view()

class ReportesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ReporteReportesSerializer    
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
reportes_create_view = ReportesListaCreateApiView.as_view()

class ReportesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ReporteReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
reportes_list_view = ReportesDetallesAPIView.as_view()

class ReportesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
reportes_actualizar_view = ReportesAztualizacionAPIView.as_view()

class ReportesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ReporteReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
        
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
reportes_eliminar_view = ReportesEliminarAPIView.as_view()




class ReportesAztualizacionClienteAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesClienteSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            return ValidationError
        return queryset
reportes_actualizar_cliente_view = ReportesAztualizacionClienteAPIView.as_view()

class ReportesAztualizacionSistemaControlCalidadAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesSistemaControlCalidadSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            return ValidationError
        return queryset
reportes_actualizar_sistema_control_calidad_view = ReportesAztualizacionSistemaControlCalidadAPIView.as_view()

class ReportesAztualizacionMaquinaControlCalidadAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesMaquinaControlCalidadSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            return ValidationError
        return queryset
reportes_actualizar_maquina_control_calidad_view = ReportesAztualizacionMaquinaControlCalidadAPIView.as_view()



class ReportesAztualizacionOpcionesAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            return ValidationError
        return queryset
reportes_actualizar_opciones_view = ReportesAztualizacionOpcionesAPIView.as_view()

class ReportesAztualizacionPruebasAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ReporteReportesPruebasSerializer
    lookup_field = 'pk'
    def get_queryset(self): 
        queryset = ReportsReporteModel.objects.all()
        if not queryset:
            return ValidationError
        return queryset
reportes_actualizar_pruebas_view = ReportesAztualizacionPruebasAPIView.as_view()




class CertificadosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = CertificadoReportesSerializer
    lookup_field = 'pk'
    def get_queryset(self):
        queryset = ReportsCertificadoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
certificados_list_view = CertificadosDetallesAPIView.as_view()

class CertificadosCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CertificadoReportesSerializer  
    def get_queryset(self):        
        queryset = ReportsCertificadoModel.objects.all()
        return queryset   

certificados_create_view = CertificadosCreateApiView.as_view()

class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No se encontraron registros', })

