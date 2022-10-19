from rest_framework import generics
# from django.http import Http404
from rest_framework.exceptions import APIException,status
from .models import ContactosModel, DepartamentoModel, OrganizacionModel, AreasModel
from .serializers import ContactosSerialezer, DepartamentoSerializer, OrganizacionSerializer,AreasSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OrganizacionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = OrganizacionSerializer
    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
organzizaciones_create_view = OrganizacionesListaCreateApiView.as_view()

class OrganizacionesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset


organzizaciones_list_view = OrganizacionesDetallesAPIView.as_view()

class OrganizacionesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()
organzizaciones_actualizar_view = OrganizacionesAztualizacionAPIView.as_view()

class OrganizacionesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = OrganizacionSerializer
    lookup_field = 'pk'

    def get_queryset(self):        
        queryset = OrganizacionModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
organzizaciones_eliminar_view = OrganizacionesEliminarAPIView.as_view()






class DepartamentosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = DepartamentoSerializer
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
departamentos_create_view = DepartamentosListaCreateApiView.as_view()

class DepartamentosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

departamentos_list_view = DepartamentosDetallesAPIView.as_view()

class DepartamentosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
departamentos_actualizar_view = DepartamentosAztualizacionAPIView.as_view()

class DepartamentosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = DepartamentoSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = DepartamentoModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
departamentos_eliminar_view = DepartamentosEliminarAPIView.as_view()





class AreasListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = AreasSerializer
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
areas_create_view = AreasListaCreateApiView.as_view()

class AreasDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
areas_list_view = AreasDetallesAPIView.as_view()

class AreasAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
areas_actualizar_view = AreasAztualizacionAPIView.as_view()

class AreasEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = AreasSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = AreasModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
areas_eliminar_view = AreasEliminarAPIView.as_view()





class ContactosListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = ContactosSerialezer
    def get_queryset(self):        
        queryset = ContactosModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
contactos_create_view = ContactosListaCreateApiView.as_view()

class ContactosDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = ContactosSerialezer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ContactosModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
contactos_list_view = ContactosDetallesAPIView.as_view()

class ContactosAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = ContactosSerialezer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ContactosModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_update(self, serializer):
        instance =serializer.save()
contactos_actualizar_view = ContactosAztualizacionAPIView.as_view()

class ContactosEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = ContactosSerialezer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = ContactosModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
contactos_eliminar_view = ContactosEliminarAPIView.as_view()




class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'No se encontraron registros', })


















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