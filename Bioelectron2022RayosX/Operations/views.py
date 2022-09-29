from rest_framework import generics
from rest_framework.response import Response
# from django.http import Http404
from .logenum import LogEnumOperaciones,OrganizacionLog
from .models import OperacionesModel,User_Operaciones_Model
from .serializers import OperacionesSerializer,UserOperacionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OperacionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = OperacionesSerializer    
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumOperaciones.OPERACION_CREATED,User_Operaciones_Model)
operaciones_create_view = OperacionListaCreateApiView.as_view()

class OperacionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        return queryset
operaciones_list_view = OperacionDetallesAPIView.as_view()

class OperacionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumOperaciones.OPERACION_UPDATED,User_Operaciones_Model)
operaciones_actualizar_view = OperacionAztualizacionAPIView.as_view()

class OperacionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
operaciones_eliminar_view = OperacionEliminarAPIView.as_view()

class OperacionesHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Operaciones_Model.objects.all()
    serializer_class = UserOperacionesSerializer
operacion_history_view = OperacionesHistoryGenericViewSet.as_view()
