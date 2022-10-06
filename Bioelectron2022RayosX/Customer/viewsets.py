from rest_framework import mixins,viewsets,mixins
from .models import ContactosModel, DepartamentoModel, OrganizacionModel,AreasModel
from .serializers import ContactosSerialezer, DepartamentoSerializer, OrganizacionSerializer,AreasSerializer
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
    def perform_update(self, serializer):
        instance =serializer.save()

class DepartamentosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = DepartamentoModel.objects.all()
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class AreasGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = AreasModel.objects.all()
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()

class ContactosGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = ContactosModel.objects.all()
    serializer_class = ContactosSerialezer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
    def perform_update(self, serializer):
        instance =serializer.save()