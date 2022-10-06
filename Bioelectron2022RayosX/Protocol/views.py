from rest_framework import generics
from rest_framework.response import Response
# from django.http import Http404
from .logenum import LogEnumProtocolos,LogEnumSecciones,LogEnumPruebaCalculo,LogEnumPruebaOpciones,LogEnumVariables,OrganizacionLog
from .models import ProtocolsModel,SeccionesModel,PruebaCalculoModel,PruebaOpcionesModel, User_Protocolos_Model, User_Pruebas_Calculo_Model, User_Pruebas_Opciones_Model, User_Secciones_Model, User_Variables_Model,VariablesModel
from .serializers import ProtocolosSerializer,SeccionesSerializer, UserProtocolosSerializer, UserPruebasCalculoSerializer, UserPruebasOpcionesSerializer, UserSeccionesSerializer, UserVariablesSerializer,VariablesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from authentication.mixins import StaffEditorPermissionMixin


class ProtocoloListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ProtocolosSerializer    
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_CREATED,User_Protocolos_Model)
protocolos_create_view = ProtocoloListaCreateApiView.as_view()

class ProtocoloDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
protocolos_list_view = ProtocoloDetallesAPIView.as_view()

class ProtocoloAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_UPDATED,User_Protocolos_Model)
protocolos_actualizar_view = ProtocoloAztualizacionAPIView.as_view()

class ProtocoloEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
protocolos_eliminar_view = ProtocoloEliminarAPIView.as_view()





class SeccionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = SeccionesSerializer    
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumSecciones.SECCION_CREATED,User_Secciones_Model)
secciones_create_view = SeccionListaCreateApiView.as_view()

class SeccionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        return queryset
secciones_list_view = SeccionDetallesAPIView.as_view()

class SeccionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumSecciones.SECCION_UPDATED,User_Secciones_Model)
secciones_actualizar_view = SeccionAztualizacionAPIView.as_view()

class SeccionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
secciones_eliminar_view = SeccionEliminarAPIView.as_view()



class PruebaCalculoListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = PruebaCalculoSerializer    
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaCalculo.PRUEBA_CALCULO_CREATED,User_Pruebas_Calculo_Model)
prueba_calculo_create_view = PruebaCalculoListaCreateApiView.as_view()

class PruebaCalculoDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        return queryset
prueba_calculo_list_view = PruebaCalculoDetallesAPIView.as_view()

class PruebaCalculoAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaCalculo.PRUEBA_CALCULO_UPDATED,User_Pruebas_Calculo_Model)
prueba_calculo_actualizar_view = PruebaCalculoAztualizacionAPIView.as_view()

class PruebaCalculoEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
prueba_calculo_eliminar_view = PruebaCalculoEliminarAPIView.as_view()



class PruebaOpcionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = PruebaOpcionesSerializer    
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaOpciones.PRUEBA_OPCION_CREATED,User_Pruebas_Opciones_Model)
pruebas_opciones_create_view = PruebaOpcionListaCreateApiView.as_view()

class PruebaOpcionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        return queryset
pruebas_opciones_list_view = PruebaOpcionDetallesAPIView.as_view()

class PruebaOpcionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumPruebaOpciones.PRUEBA_OPCION_UPDATED,User_Pruebas_Opciones_Model)
pruebas_opciones_actualizar_view = PruebaOpcionAztualizacionAPIView.as_view()

class PruebaOpcionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
pruebas_opciones_eliminar_view = PruebaOpcionEliminarAPIView.as_view()



class VariableListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = VariablesSerializer    
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumVariables.VARIABLE_CREATED,User_Variables_Model)
variables_create_view = VariableListaCreateApiView.as_view()

class VariableDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        return queryset
variables_list_view = VariableDetallesAPIView.as_view()

class VariableAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumVariables.VARIABLE_UPDATED,User_Variables_Model)
variables_actualizar_view = VariableAztualizacionAPIView.as_view()

class VariableEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
variables_eliminar_view = VariableEliminarAPIView.as_view()



class ProtocoloListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ProtocolosSerializer    
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_CREATED,User_Protocolos_Model)
protocolos_create_view = ProtocoloListaCreateApiView.as_view()

class ProtocoloDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
protocolos_list_view = ProtocoloDetallesAPIView.as_view()

class ProtocoloAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumProtocolos.PROTOCOLO_UPDATED,User_Protocolos_Model)
protocolos_actualizar_view = ProtocoloAztualizacionAPIView.as_view()

class ProtocoloEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
protocolos_eliminar_view = ProtocoloEliminarAPIView.as_view()




class ProtocolosHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Protocolos_Model.objects.all()
    serializer_class = UserProtocolosSerializer
protocolo_history_view = ProtocolosHistoryGenericViewSet.as_view()

class SeccionesHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Secciones_Model.objects.all()
    serializer_class = UserSeccionesSerializer
seccion_history_view = SeccionesHistoryGenericViewSet.as_view()

class PruebasCalculoHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Pruebas_Calculo_Model.objects.all()
    serializer_class = UserPruebasCalculoSerializer
prueba_calculo_history_view = PruebasCalculoHistoryGenericViewSet.as_view()

class PruebasOpcionesHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Pruebas_Opciones_Model.objects.all()
    serializer_class = UserPruebasOpcionesSerializer
prueba_opcion_history_view = PruebasOpcionesHistoryGenericViewSet.as_view()

class VariablesHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Variables_Model.objects.all()
    serializer_class = UserVariablesSerializer
variable_history_view = VariablesHistoryGenericViewSet.as_view()

