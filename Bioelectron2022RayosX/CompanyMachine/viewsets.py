from rest_framework import mixins,viewsets,mixins
from rest_framework.exceptions import APIException,status
from .models import CalibracionesModel, MedidoresModel
from .serializers import CalibracionesSerializer, MedidoresSerializer
from authentication.mixins import StaffEditorPermissionMixin

class CalibracionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):       
        queryset = CalibracionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class MedidoresGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def get_queryset(self):       
        queryset = MedidoresModel.objects.all()
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


