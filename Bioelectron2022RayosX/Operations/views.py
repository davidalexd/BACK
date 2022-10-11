from rest_framework import generics
from rest_framework.exceptions import APIException,status
# from django.http import Http404
from .models import OperacionesModel
from .serializers import OperacionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OperacionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = OperacionesSerializer    
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
operaciones_create_view = OperacionListaCreateApiView.as_view()

class OperacionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
operaciones_list_view = OperacionDetallesAPIView.as_view()

class OperacionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
operaciones_actualizar_view = OperacionAztualizacionAPIView.as_view()

class OperacionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
operaciones_eliminar_view = OperacionEliminarAPIView.as_view()

class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No data is available', })
