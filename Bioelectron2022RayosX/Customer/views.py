from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .logenum import LogEnumOrganizaciones
from .models import OrganizacionModel, User_Organizaciones_Model
from .serializers import OrganizacionSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OrganizacionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_CREATED,User_Organizaciones_Model)
organzizaciones_create_view = OrganizacionesListaCreateApiView.as_view()

class OrganizacionesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
organzizaciones_list_view = OrganizacionesDetallesAPIView.as_view()

class OrganizacionesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumOrganizaciones.ORGANIZACION_UPDATED,User_Organizaciones_Model)
organzizaciones_actualizar_view = OrganizacionesAztualizacionAPIView.as_view()

class OrganizacionesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    queryset = OrganizacionModel.objects.all()
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
organzizaciones_eliminar_view = OrganizacionesEliminarAPIView.as_view()

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(organizacion=instance,user=author.request.user,context=message+author.request.user.username)


# class OrganizacionMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = OrganizacionModel.objects.all()
#     serializer_class = OrganizacionSerializer
#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [IsStaffEditorPermission]
#     lookup_field = 'pk'

#     def get(self,request,*args,**kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return self.list(request,*args,**kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def perform_create(self, serializer):
#         serializer.save()
# organizaciones_mixin_view = OrganizacionMixinView.as_view()

# class OrganizacionMixinUpdateView(mixins.ListModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = OrganizacionModel.objects.all()
#     serializer_class = OrganizacionSerializer
#     lookup_field = 'pk'

#     def get(self,request,*args,**kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request,*args,**kwargs)
#         return self.list(request,*args,**kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def perform_update(self, serializer):
#         serializer.save()

# organizaciones_mixin_update = OrganizacionMixinUpdateView.as_view()

# @api_view(['GET','POST'])
# def organzicion_alt_view(request,pk=None, *args, **kwargs):
    # method = request.method

    # if method == 'GET':
    #     if pk is not None:
    #         obj = get_object_or_404(OrganizacionModel,id=pk)
    #         data = OrganizacionSerializer(obj,many=False).data
    #         return Response(data)
    #     queryset = OrganizacionModel.objects.all()
    #     data = OrganizacionSerializer(queryset,many=True).data
    #     return Response(data)
    # if method == 'POST':
    #     serializer = OrganizacionSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception = True):
    #         return Response(serializer.data)
    #     return Response({"invalid":"not good data"},status=400)