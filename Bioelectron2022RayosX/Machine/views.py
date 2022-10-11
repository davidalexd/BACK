from rest_framework import generics
from rest_framework.exceptions import APIException,status
# from django.http import Http404
from .models import SistemaModel,TuboModel
from .serializers import SistemaSerializer,TuboSerializer
from authentication.mixins import StaffEditorPermissionMixin

class SistemasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = SistemaSerializer
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
sistemas_create_view = SistemasListaCreateApiView.as_view()

class SistemasDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

sistemas_list_view = SistemasDetallesAPIView.as_view()

class SistemasAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
sistemas_actualizar_view = SistemasAztualizacionAPIView.as_view()

class SistemasEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
sistemas_eliminar_view = SistemasEliminarAPIView.as_view()




class TubosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = TuboSerializer
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
tubos_create_view = TubosListaCreateApiView.as_view()

class TubosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = TuboSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

tubos_list_view = TubosDetallesAPIView.as_view()

class TubosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = TuboSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
tubos_actualizar_view = TubosAztualizacionAPIView.as_view()

class TubosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = TuboSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
tubos_eliminar_view = TubosEliminarAPIView.as_view()

class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No data is available', })



