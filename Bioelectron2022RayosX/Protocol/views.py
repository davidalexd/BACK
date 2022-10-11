from rest_framework import generics
from rest_framework.exceptions import APIException,status
# from django.http import Http404
from .models import ProtocolsModel,SeccionesModel,PruebaCalculoModel,PruebaOpcionesModel,VariablesModel
from .serializers import ProtocolosSerializer,SeccionesSerializer,VariablesSerializer,PruebaCalculoSerializer,PruebaOpcionesSerializer
from authentication.mixins import StaffEditorPermissionMixin


class ProtocoloListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ProtocolosSerializer    
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
protocolos_create_view = ProtocoloListaCreateApiView.as_view()

class ProtocoloDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
protocolos_list_view = ProtocoloDetallesAPIView.as_view()

class ProtocoloAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
protocolos_actualizar_view = ProtocoloAztualizacionAPIView.as_view()

class ProtocoloEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
        
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
protocolos_eliminar_view = ProtocoloEliminarAPIView.as_view()





class SeccionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = SeccionesSerializer    
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
secciones_create_view = SeccionListaCreateApiView.as_view()

class SeccionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
secciones_list_view = SeccionDetallesAPIView.as_view()

class SeccionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
secciones_actualizar_view = SeccionAztualizacionAPIView.as_view()

class SeccionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = SeccionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = SeccionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
secciones_eliminar_view = SeccionEliminarAPIView.as_view()



class PruebaCalculoListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = PruebaCalculoSerializer    
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
prueba_calculo_create_view = PruebaCalculoListaCreateApiView.as_view()

class PruebaCalculoDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
prueba_calculo_list_view = PruebaCalculoDetallesAPIView.as_view()

class PruebaCalculoAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
prueba_calculo_actualizar_view = PruebaCalculoAztualizacionAPIView.as_view()

class PruebaCalculoEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = PruebaCalculoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaCalculoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
prueba_calculo_eliminar_view = PruebaCalculoEliminarAPIView.as_view()



class PruebaOpcionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = PruebaOpcionesSerializer    
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
pruebas_opciones_create_view = PruebaOpcionListaCreateApiView.as_view()

class PruebaOpcionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
pruebas_opciones_list_view = PruebaOpcionDetallesAPIView.as_view()

class PruebaOpcionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
pruebas_opciones_actualizar_view = PruebaOpcionAztualizacionAPIView.as_view()

class PruebaOpcionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = PruebaOpcionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = PruebaOpcionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
pruebas_opciones_eliminar_view = PruebaOpcionEliminarAPIView.as_view()



class VariableListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = VariablesSerializer    
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
variables_create_view = VariableListaCreateApiView.as_view()

class VariableDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
variables_list_view = VariableDetallesAPIView.as_view()

class VariableAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
variables_actualizar_view = VariableAztualizacionAPIView.as_view()

class VariableEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = VariablesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = VariablesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
variables_eliminar_view = VariableEliminarAPIView.as_view()



class ProtocoloListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ProtocolosSerializer    
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
protocolos_create_view = ProtocoloListaCreateApiView.as_view()

class ProtocoloDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
protocolos_list_view = ProtocoloDetallesAPIView.as_view()

class ProtocoloAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
protocolos_actualizar_view = ProtocoloAztualizacionAPIView.as_view()

class ProtocoloEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ProtocolosSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ProtocolsModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
protocolos_eliminar_view = ProtocoloEliminarAPIView.as_view()


class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No data is available', })
