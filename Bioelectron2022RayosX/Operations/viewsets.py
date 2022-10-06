from .logenum import LogEnumOperaciones,OrganizacionLog
from rest_framework import mixins,viewsets,mixins
from .models import OperacionesModel,User_Operaciones_Model
from .serializers import OperacionesSerializer,UserOperacionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OperacionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumOperaciones.OPERACION_CREATED,User_Operaciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumOperaciones.OPERACION_UPDATED,User_Operaciones_Model)



class SistemasHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Operaciones_Model.objects.all()
    serializer_class = UserOperacionesSerializer