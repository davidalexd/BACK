from rest_framework import mixins,viewsets,generics,mixins,permissions,authentication
from .models import OrganizacionModel,User_Organizaciones_Model
from .serializers import OrganizacionSerializer
from authentication.mixins import StaffEditorPermissionMixin
from .logenum import LogEnumOrganizaciones

class OrganizacionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_CREATED,User_Organizaciones_Model)
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_UPDATED,User_Organizaciones_Model)

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(organizacion=instance,user=author.request.user,context=message+author.request.user.username)

