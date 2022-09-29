from .logenum import LogEnumProtocolos,LogEnumSecciones,LogEnumPruebas,LogEnumPruebaCalculo,LogEnumPruebaOpciones,LogEnumVariables,OrganizacionLog
from rest_framework import mixins,viewsets,mixins
from .models import ProtocolsModel,SeccionesModel,PruebaCalculoModel,PruebasModel,PruebaOpcionesModel, User_Protocolos_Model, User_Pruebas_Calculo_Model, User_Pruebas_Model, User_Pruebas_Opciones_Model, User_Secciones_Model, User_Variables_Model,VariablesModel
from .serializers import ProtocolosSerializer,SeccionesSerializer, UserProtocolosSerializer, UserPruebasCalculoSerializer, UserPruebasOpcionesSerializer, UserPruebasSerializer, UserSeccionesSerializer, UserVariablesSerializer,VariablesSerializer,PruebasSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class ProtocolosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_CREATED,User_Protocolos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_UPDATED,User_Protocolos_Model)

class SeccionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumSecciones.SECCION_CREATED,User_Secciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumSecciones.SECCION_UPDATED,User_Secciones_Model)

class PruebasGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = PruebasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebasModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebas.PRUEBA_CREATED,User_Pruebas_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebas.PRUEBA_UPDATED,User_Pruebas_Model)

class PruebasCalculoGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaCalculo.PRUEBA_CALCULO_CREATED,User_Pruebas_Calculo_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaCalculo.PRUEBA_CALCULO_UPDATED,User_Pruebas_Calculo_Model)

class PruebasOpcionGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaOpciones.PRUEBA_OPCION_CREATED,User_Pruebas_Opciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaOpciones.PRUEBA_OPCION_UPDATED,User_Pruebas_Opciones_Model)

class VariableGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumVariables.VARIABLE_CREATED,User_Variables_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumVariables.VARIABLE_UPDATED,User_Variables_Model)

class ProtocolosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_CREATED,User_Protocolos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_UPDATED,User_Protocolos_Model)

class ProtocoloHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Protocolos_Model.objects.all()
    serializer_class = UserProtocolosSerializer

class VariablesHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Variables_Model.objects.all()
    serializer_class = UserVariablesSerializer

class SeccionesHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Secciones_Model.objects.all()
    serializer_class = UserSeccionesSerializer

class PruebaHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Pruebas_Model.objects.all()
    serializer_class = UserPruebasSerializer

class PruebaCalculoHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Pruebas_Calculo_Model.objects.all()
    serializer_class = UserPruebasCalculoSerializer

class PruebaOpcionHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Pruebas_Opciones_Model.objects.all()
    serializer_class = UserPruebasOpcionesSerializer