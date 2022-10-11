from rest_framework.exceptions import APIException,status
from rest_framework import mixins,viewsets,mixins
from .models import OperacionesModel
from .serializers import OperacionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OperacionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
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
