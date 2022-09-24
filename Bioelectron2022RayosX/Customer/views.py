from rest_framework import generics
from .models import OrganizacionModel
from .serializers import OrganizacionSerializer

class OrganizacionesCreateApiView(generics.CreateAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer

    # def perform_create(self, serializer):
        # serializer.save(user=self.request.user)


organzizaciones_create_view = OrganizacionesCreateApiView.as_view()

class OrganizacionesDetallesAPIView(generics.RetrieveAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer


organzizaciones_list_view = OrganizacionesDetallesAPIView.as_view()

