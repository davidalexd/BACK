from rest_framework import generics
from rest_framework.response import Response
# from django.http import Http404
from .logenum import LogEnumCalibraciones, LogEnumMedidores,OrganizacionLog
from .models import CalibracionesModel, MedidoresModel,User_Calibraciones_Model, User_Medidores_Model 
from .serializers import CalibracionesSerializer, MedidoresSerializer, UserCalibracionesSerializer, UserMedidoresSerializer
from authentication.mixins import StaffEditorPermissionMixin

class CalibracionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CalibracionesSerializer
    def get_queryset(self):        
        queryset = CalibracionesModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumCalibraciones.CALIBRACION_CREATED,User_Calibraciones_Model)
calibraciones_create_view = CalibracionesListaCreateApiView.as_view()

class CalibracionesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = CalibracionesModel.objects.all()
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
calibraciones_list_view = CalibracionesDetallesAPIView.as_view()

class CalibracionesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    queryset = CalibracionesModel.objects.all()
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = self.save()
        OrganizacionLog(self,instance,LogEnumCalibraciones.CALIBRACION_UPDATED,User_Calibraciones_Model)
calibraciones_actualizar_view = CalibracionesAztualizacionAPIView.as_view()

class CalibracionesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    queryset = CalibracionesModel.objects.all()
    serializer_class = CalibracionesSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
calibraciones_eliminar_view = CalibracionesEliminarAPIView.as_view()




class MedidoresListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = MedidoresSerializer
    def get_queryset(self):        
        queryset = MedidoresModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumMedidores.MEDIDOR_CREATED,User_Medidores_Model)
medidores_create_view = MedidoresListaCreateApiView.as_view()

class MedidoresDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = MedidoresModel.objects.all()
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
medidores_list_view = MedidoresDetallesAPIView.as_view()

class MedidoresAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    queryset = MedidoresModel.objects.all()
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = self.save()
        OrganizacionLog(self,instance,LogEnumMedidores.MEDIDOR_UPDATED,User_Medidores_Model)
medidores_actualizar_view = MedidoresAztualizacionAPIView.as_view()

class MedidoresEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    queryset = MedidoresModel.objects.all()
    serializer_class = MedidoresSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
medidores_eliminar_view = MedidoresEliminarAPIView.as_view()



class CalibracionesHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Calibraciones_Model.objects.all()
    serializer_class = UserCalibracionesSerializer
calibracion_history_view = CalibracionesHistoryGenericViewSet.as_view()

class MedidoresHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Medidores_Model.objects.all()
    serializer_class = UserMedidoresSerializer
medidor_history_view = MedidoresHistoryGenericViewSet.as_view()




