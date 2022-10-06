from rest_framework import mixins,viewsets,mixins
from .models import ContactosModel, DepartamentoModel, OrganizacionModel,AreasModel, User_Contactos_Model, User_Departamentos_Model,User_Organizaciones_Model,User_Areas_Model
from .serializers import ContactosSerialezer, DepartamentoSerializer, OrganizacionSerializer,AreasSerializer, UserAreaSerializer, UserContactosSerializer, UserDepartamentoSerializer, UserOrganizacionSerializer
from authentication.mixins import StaffEditorPermissionMixin
from .logenum import LogEnumContactos, LogEnumOrganizaciones,LogEnumDepartamentos,LogEnumAreas,OrganizacionLog

class OrganizacionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        return queryset
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_CREATED,User_Organizaciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_UPDATED,User_Organizaciones_Model)

class DepartamentosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = DepartamentoModel.objects.all()
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumDepartamentos.DEPARTAMENTO_CREATED,User_Departamentos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumDepartamentos.DEPARTAMENTO_UPDATED,User_Departamentos_Model)

class AreasGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = AreasModel.objects.all()
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumAreas.AREA_CREATED,User_Areas_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumAreas.AREA_UPDATED,User_Areas_Model)

class ContactosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = ContactosModel.objects.all()
    serializer_class = ContactosSerialezer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumContactos.CONTACTO_CREATED,User_Contactos_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumContactos.CONTACTO_UPDATED,User_Contactos_Model)

class AreasHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Areas_Model.objects.all()
    serializer_class = UserAreaSerializer

class DepartamentosHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Departamentos_Model.objects.all()
    serializer_class = UserDepartamentoSerializer

class OrganizacionHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Organizaciones_Model.objects.all()
    serializer_class = UserOrganizacionSerializer


class ContactosHistoryGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = User_Contactos_Model.objects.all()
    serializer_class = UserContactosSerializer