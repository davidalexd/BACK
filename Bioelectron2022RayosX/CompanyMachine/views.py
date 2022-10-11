from rest_framework import generics
from rest_framework.exceptions import APIException,status
# from django.http import Http404
from .models import CalibracionesModel, MedidoresModel
from .serializers import CalibracionesSerializer, MedidoresSerializer
from authentication.mixins import StaffEditorPermissionMixin

class CalibracionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CalibracionesSerializer
    def get_queryset(self):        
        queryset = CalibracionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
calibraciones_create_view = CalibracionesListaCreateApiView.as_view()

class CalibracionesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = CalibracionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

calibraciones_list_view = CalibracionesDetallesAPIView.as_view()

class CalibracionesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = CalibracionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()
calibraciones_actualizar_view = CalibracionesAztualizacionAPIView.as_view()

class CalibracionesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'

    def get_queryset(self):        
        queryset = CalibracionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
calibraciones_eliminar_view = CalibracionesEliminarAPIView.as_view()




class MedidoresListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = MedidoresSerializer
    def get_queryset(self):        
        queryset = MedidoresModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
medidores_create_view = MedidoresListaCreateApiView.as_view()

class MedidoresDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = MedidoresModel.objects.all()
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = MedidoresModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

medidores_list_view = MedidoresDetallesAPIView.as_view()

class MedidoresAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):

    serializer_class = MedidoresSerializer
    lookup_field = 'pk'

    def get_queryset(self):        
        queryset = MedidoresModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()
medidores_actualizar_view = MedidoresAztualizacionAPIView.as_view()

class MedidoresEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = MedidoresModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
medidores_eliminar_view = MedidoresEliminarAPIView.as_view()



class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No data is available', })



