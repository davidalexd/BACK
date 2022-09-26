from rest_framework import mixins,viewsets,generics,mixins,permissions,authentication
from .models import OrganizacionModel
from .serializers import OrganizacionSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OrganizacionesGenericViewSet(StaffEditorPermissionMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'