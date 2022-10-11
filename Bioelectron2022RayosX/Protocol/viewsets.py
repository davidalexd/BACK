from rest_framework import mixins,viewsets,mixins
from rest_framework.exceptions import APIException,status
from .models import ProtocolsModel,SeccionesModel,PruebaCalculoModel,PruebaOpcionesModel,VariablesModel
from .serializers import ProtocolosSerializer,SeccionesSerializer,VariablesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class ProtocolosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class SeccionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class PruebasCalculoGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class PruebasOpcionGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class VariableGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class ProtocolosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()


class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No data is available', })
