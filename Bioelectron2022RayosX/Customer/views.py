from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .logenum import LogEnumDepartamentos, LogEnumOrganizaciones,LogEnumAreas,OrganizacionLog
from .models import DepartamentoModel, OrganizacionModel, AreasModel, User_Departamentos_Model, User_Organizaciones_Model, User_Areas_Model
from .serializers import DepartamentoSerializer, OrganizacionSerializer,AreasSerializer, UserAreaSerializer, UserDepartamentoSerializer, UserOrganizacionSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OrganizacionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = OrganizacionSerializer
    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        return queryset

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






class DepartamentosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumDepartamentos.DEPARTAMENTO_CREATED,User_Departamentos_Model)
departamentos_create_view = DepartamentosListaCreateApiView.as_view()

class DepartamentosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        return queryset
departamentos_list_view = DepartamentosDetallesAPIView.as_view()

class DepartamentosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    queryset = DepartamentoModel.objects.all()
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumDepartamentos.DEPARTAMENTO_UPDATED,User_Departamentos_Model)
departamentos_actualizar_view = DepartamentosAztualizacionAPIView.as_view()

class DepartamentosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
departamentos_eliminar_view = DepartamentosEliminarAPIView.as_view()



class AreasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = AreasSerializer
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        OrganizacionLog(self,instance,LogEnumAreas.AREA_CREATED,User_Areas_Model)
areas_create_view = AreasListaCreateApiView.as_view()

class AreasDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        return queryset
areas_list_view = AreasDetallesAPIView.as_view()

class AreasAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    queryset = DepartamentoModel.objects.all()
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
        OrganizacionLog(self,instance,LogEnumAreas.AREA_UPDATED,User_Areas_Model)
areas_actualizar_view = AreasAztualizacionAPIView.as_view()

class AreasEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
areas_eliminar_view = AreasEliminarAPIView.as_view()





class AreasHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Areas_Model.objects.all()
    serializer_class = UserAreaSerializer
areas_history_view = AreasHistoryGenericViewSet.as_view()

class DepartamentosHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Departamentos_Model.objects.all()
    serializer_class = UserDepartamentoSerializer
departamento_history_view = DepartamentosHistoryGenericViewSet.as_view()

class OrganizacionHistoryGenericViewSet(StaffEditorPermissionMixin,generics.ListAPIView):
    queryset = User_Organizaciones_Model.objects.all()
    serializer_class = UserOrganizacionSerializer
organizacion_history_view = OrganizacionHistoryGenericViewSet.as_view()
























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