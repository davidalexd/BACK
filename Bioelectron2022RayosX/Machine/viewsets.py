from rest_framework import mixins,viewsets,mixins
from rest_framework.exceptions import APIException,status
from .models import SistemaModel, TuboModel
from .serializers import SistemaSerializer, TuboSerializer
from authentication.mixins import StaffEditorPermissionMixin

class SistemasGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class TubosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = TuboSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()
        
class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No se encontraron registros', })

