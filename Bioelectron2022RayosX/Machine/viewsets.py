from rest_framework import mixins,viewsets,mixins
from .models import SistemaModel, TuboModel, User_sistemas_Model, User_tubos_Model
from .serializers import SistemaSerializer, TuboSerializer, UserTubosSerializer, UsersistemasSerializer
from authentication.mixins import StaffEditorPermissionMixin
from .logenum import LogEnumSistemas,LogEnumTubos,OrganizacionLog

class SistemasGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumSistemas.SISTEMA_CREATED,User_sistemas_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumSistemas.SISTEMA_UPDATED,User_sistemas_Model)

class TubosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = TuboSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumTubos.TUBO_CREATED,User_tubos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumTubos.TUBO_UPDATED,User_tubos_Model)



class SistemasHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_sistemas_Model.objects.all()
    serializer_class = UsersistemasSerializer


class TubosHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_tubos_Model.objects.all()
    serializer_class = UserTubosSerializer