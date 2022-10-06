from rest_framework import mixins,viewsets,mixins
from .models import CalibracionesModel, MedidoresModel, User_Calibraciones_Model, User_Medidores_Model
from .serializers import CalibracionesSerializer, MedidoresSerializer, UserCalibracionesSerializer, UserMedidoresSerializer
from authentication.mixins import StaffEditorPermissionMixin
from .logenum import LogEnumCalibraciones, LogEnumMedidores,OrganizacionLog

class CalibracionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = CalibracionesModel.objects.all()
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumCalibraciones.CALIBRACION_CREATED,User_Calibraciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumCalibraciones.CALIBRACION_UPDATED,User_Calibraciones_Model)

class MedidoresGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = MedidoresModel.objects.all()
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumMedidores.MEDIDOR_CREATED,User_Medidores_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumMedidores.MEDIDOR_UPDATED,User_Medidores_Model)


class CalibracionesHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Calibraciones_Model.objects.all()
    serializer_class = UserCalibracionesSerializer

class MedidoresHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Medidores_Model.objects.all()
    serializer_class = UserMedidoresSerializer