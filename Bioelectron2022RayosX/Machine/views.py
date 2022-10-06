from rest_framework import generics
from rest_framework.response import Response
# from django.http import Http404
from .logenum import LogEnumSistemas, LogEnumTubos,OrganizacionLog
from .models import SistemaModel,TuboModel,User_sistemas_Model,User_tubos_Model
from .serializers import SistemaSerializer,TuboSerializer,UsersistemasSerializer,UserTubosSerializer
from authentication.mixins import StaffEditorPermissionMixin

class SistemasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = SistemaSerializer
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumSistemas.SISTEMA_CREATED,User_sistemas_Model)
sistemas_create_view = SistemasListaCreateApiView.as_view()

class SistemasDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        return queryset
sistemas_list_view = SistemasDetallesAPIView.as_view()

class SistemasAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumSistemas.SISTEMA_UPDATED,User_sistemas_Model)
sistemas_actualizar_view = SistemasAztualizacionAPIView.as_view()

class SistemasEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = SistemaSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SistemaModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
sistemas_eliminar_view = SistemasEliminarAPIView.as_view()




class TubosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = TuboSerializer
    def get_queryset(self):        
        queryset = TuboModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumTubos.TUBO_CREATED,User_tubos_Model)
tubos_create_view = TubosListaCreateApiView.as_view()

class TubosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = TuboSerializer
    queryset = TuboModel.objects.all()
    lookup_field = 'pk'
tubos_list_view = TubosDetallesAPIView.as_view()

class TubosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = TuboSerializer
    queryset = TuboModel.objects.all()
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumTubos.TUBO_UPDATED,User_tubos_Model)
tubos_actualizar_view = TubosAztualizacionAPIView.as_view()

class TubosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = TuboSerializer
    queryset = TuboModel.objects.all()
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
tubos_eliminar_view = TubosEliminarAPIView.as_view()



class SistemasHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_sistemas_Model.objects.all()
    serializer_class = UsersistemasSerializer
sistema_history_view = SistemasHistoryGenericViewSet.as_view()

class TubosHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_tubos_Model.objects.all()
    serializer_class = UserTubosSerializer
tubo_history_view = TubosHistoryGenericViewSet.as_view()




