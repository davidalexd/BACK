import json
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from rest_framework import status
from rest_framework.exceptions import APIException,status


# from django.http import Http404
from .models import CategoryOperacionesModel, OperacionesModel, VariablesModel
from .serializers import CategoriaOperacionesSerializer, OperacionesSerializer, VariablesSerializer
from authentication.mixins import StaffEditorPermissionMixin

class OperacionListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = OperacionesSerializer    
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
operaciones_create_view = OperacionListaCreateApiView.as_view()

class OperacionDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
operaciones_list_view = OperacionDetallesAPIView.as_view()

class OperacionAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
operaciones_actualizar_view = OperacionAztualizacionAPIView.as_view()

class OperacionEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = OperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = OperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
operaciones_eliminar_view = OperacionEliminarAPIView.as_view()


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



class CategoriaOperacionesListaCreateApiView(StaffEditorPermissionMixin,generics.ListCreateAPIView):
    serializer_class = CategoriaOperacionesSerializer    
    def get_queryset(self):        
        queryset = CategoryOperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
categoria_operaciones_create_view = CategoriaOperacionesListaCreateApiView.as_view()

class CategoriaOperacionesDetallesAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    serializer_class = CategoriaOperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = CategoryOperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
categoria_operaciones_list_view = CategoriaOperacionesDetallesAPIView.as_view()

class CategoriaOperacionesAztualizacionAPIView(StaffEditorPermissionMixin,generics.RetrieveUpdateAPIView):
    serializer_class = CategoriaOperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = CategoryOperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    
    def perform_update(self, serializer):
        instance =serializer.save()
categoria_operaciones_actualizar_view = CategoriaOperacionesAztualizacionAPIView.as_view()

class CategoriaOperacionesEliminarAPIView(StaffEditorPermissionMixin,generics.RetrieveDestroyAPIView):
    serializer_class = CategoriaOperacionesSerializer
    lookup_field = 'pk'
    def get_queryset(self):        
        queryset = CategoryOperacionesModel.objects.all()
        if not queryset:
            raise ValidationError
        return queryset
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
categoria_operaciones_eliminar_view = CategoriaOperacionesEliminarAPIView.as_view()




# Vistas de soluciones a formulas

from Functions.Services.Fluoroscopia.fluoroscopia_exactitud_tiempo_exposicion import fluoroscopia_exactitud_tiempo_exposicion
from Functions.Services.Fluoroscopia.fluoroscopia_filtracion_capa_hemireductora import fluoroscopia_filtracion_capa_hemireductora
from Functions.Services.Fluoroscopia.fluoroscopia_repetibilidad_tension import fluoroscopia_repetibilidad_tension
from Functions.Services.Fluoroscopia.fluoroscopia_exactitud_tension import fluoroscopia_exactitud_tension
from Functions.Services.Fluoroscopia.fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector import fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector
from Functions.Services.Fluoroscopia.fluoroscopia_tamano_campo_entrada_detector_imagen import fluoroscopia_tamano_campo_entrada_detector_imagen
from Functions.Services.Fluoroscopia.fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen import fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen
from Functions.Services.Fluoroscopia.fluoroscopia_distorsion_geometrica import fluoroscopia_distorsion_geometrica
from Functions.Services.Fluoroscopia.fluoroscopia_alineacion_rayos_x_haz_luminoso import fluoroscopia_alineacion_rayos_x_haz_luminoso
from Functions.Services.Fluoroscopia.fluoroscopia_repetibilidad_tiempo_exposicion import fluoroscopia_repetibilidad_tiempo_exposicion
from Functions.Services.Fluoroscopia.fluoroscopia_repetibilidad_rendimiento import fluoroscopia_repetibilidad_rendimiento
from Functions.Services.Fluoroscopia.fluoroscopia_valor_rendimiento import fluoroscopia_valor_rendimiento
from Functions.Services.Fluoroscopia.fluoroscopia_variacion_rendimiento_carga import fluoroscopia_variacion_rendimiento_carga
from Functions.Services.RayosXDental.dental_exactitud_tension import dental_exactitud_tension
from Functions.Services.RayosXDental.dental_exactitud_tiempo_exposicion_1 import dental_exactitud_tiempo_exposicion_1
from Functions.Services.RayosXDental.dental_exactitud_tiempo_exposicion_2 import dental_exactitud_tiempo_exposicion_2
from Functions.Services.RayosXDental.dental_filtracion import dental_filtracion
from Functions.Services.RayosXDental.dental_kerma_aire_entrada_paciente import dental_kerma_aire_entrada_paciente
from Functions.Services.RayosXDental.dental_minima_distancia_foco_piel import dental_minima_distancia_foco_piel
from Functions.Services.RayosXDental.dental_repetibilidad_rendimiento import dental_repetibilidad_rendimiento
from Functions.Services.RayosXDental.dental_repetibilidad_tension import dental_repetibilidad_tension
from Functions.Services.RayosXDental.dental_repetibilidad_tiempo_exposicion import dental_repetibilidad_tiempo_exposicion
from Functions.Services.RayosXDental.dental_tamano_campo_extremo_localizador import dental_tamano_campo_extremo_localizador
from Functions.Services.RayosXDental.dental_valor_rendimiento import dental_valor_rendimiento
from Functions.Services.RayosXDental.dental_variacion_rendimiento import dental_variacion_rendimiento


class fluoroscopia_alineacionrayosxhazluminoso(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_alineacion_rayos_x_haz_luminoso((data_entrante[0]),(data_entrante[1]),(data_entrante[2]),(data_entrante[3]),(data_entrante[4]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_alineacion_rayos_x_haz_luminoso = fluoroscopia_alineacionrayosxhazluminoso.as_view()

class fluoroscopia_distorsiongeometrica(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_distorsion_geometrica((data_entrante[0]),(data_entrante[1]),(data_entrante[2]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_distorsion_geometrica = fluoroscopia_distorsiongeometrica.as_view()

class fluoroscopia_ortogonalidadhazrayosxreceptor_imagen(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen((data_entrante[0]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen = fluoroscopia_ortogonalidadhazrayosxreceptor_imagen.as_view()

class fluoroscopia_tamanocampoentradadetectorimagen(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_tamano_campo_entrada_detector_imagen((data_entrante[0]),(data_entrante[1]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_tamano_campo_entrada_detector_imagen = fluoroscopia_tamanocampoentradadetectorimagen.as_view()


class fluoroscopia_coincidenciacamporadiacionareavisualizadadetector(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector((data_entrante[0]),(data_entrante[1]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector = fluoroscopia_coincidenciacamporadiacionareavisualizadadetector.as_view()

class fluoroscopia_exactitudtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_exactitud_tension((data_entrante[0]),(data_entrante[1]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_exactitud_tension = fluoroscopia_exactitudtension.as_view()

class fluoroscopia_repetibilidadtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_tension(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_tension = fluoroscopia_repetibilidadtension.as_view()

class fluoroscopia_filtracioncapahemireductora(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_filtracion_capa_hemireductora(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_filtracion_capa_hemireductora = fluoroscopia_filtracioncapahemireductora.as_view()


class fluoroscopia_exactitudtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_exactitud_tiempo_exposicion((data_entrante[0]),(data_entrante[1]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_exactitud_tiempo_exposicion = fluoroscopia_exactitudtiempoexposicion.as_view()

class fluoroscopia_repetibilidadtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_tiempo_exposicion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_tiempo_exposicion = fluoroscopia_repetibilidadtiempoexposicion.as_view()


class fluoroscopia_valorrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_valor_rendimiento(data_entrante[0],(data_entrante[1]),(data_entrante[2]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_valor_rendimiento = fluoroscopia_valorrendimiento.as_view()

class fluoroscopia_repetibilidadrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_rendimiento(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_rendimiento= fluoroscopia_repetibilidadrendimiento.as_view()

class fluoroscopia_variacionrendimientocarga(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_variacion_rendimiento_carga(data_entrante[0],data_entrante[1],(data_entrante[2]),(data_entrante[3]),(data_entrante[4]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_variacion_rendimiento_carga= fluoroscopia_variacionrendimientocarga.as_view()
  


# dental


class dental_exactitudtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_exactitud_tension(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_exactitud_tension= dental_exactitudtension.as_view()
 
class dental_exactitudtiempoexposicion_1(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_exactitud_tiempo_exposicion_1(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_exactitud_tiempo_exposicion_1= dental_exactitudtiempoexposicion_1.as_view()

class dental_exactitudtiempoexposicion_2(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_exactitud_tiempo_exposicion_2(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_exactitud_tiempo_exposicion_2= dental_exactitudtiempoexposicion_2.as_view()

class dental_filtracionview(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_filtracion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_filtracion= dental_filtracionview.as_view()

class dental_kermaaireentradapaciente(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_kerma_aire_entrada_paciente(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_kerma_aire_entrada_paciente= dental_kermaaireentradapaciente.as_view()

class dental_minimadistanciafocopiel(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_minima_distancia_foco_piel(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_minima_distancia_foco_piel= dental_minimadistanciafocopiel.as_view()

class dental_repetibilidadrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_repetibilidad_rendimiento(data_entrante[0],data_entrante[1],(data_entrante[2]),data_entrante[3])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_repetibilidad_rendimiento= dental_repetibilidadrendimiento.as_view()

class dental_repetibilidadtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_repetibilidad_tension(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_repetibilidad_tension= dental_repetibilidadtension.as_view()

class dental_repetibilidadtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_repetibilidad_tiempo_exposicion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_repetibilidad_tiempo_exposicion= dental_repetibilidadtiempoexposicion.as_view()

class dental_tamanocampoextremolocalizador(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_tamano_campo_extremo_localizador(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_tamano_campo_extremo_localizador= dental_tamanocampoextremolocalizador.as_view()

class dental_valorrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_valor_rendimiento(data_entrante[0],data_entrante[1],(data_entrante[2]),(data_entrante[3]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_valor_rendimiento= dental_valorrendimiento.as_view()


class dental_variacionrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = dental_variacion_rendimiento(data_entrante[0],data_entrante[1],(data_entrante[2]),(data_entrante[3]),(data_entrante[4]),(data_entrante[5]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_dental_variacion_rendimiento= dental_variacionrendimiento.as_view()



from Functions.Services.RayosXGeneral.general_dosis_superficie_paciente import general_dosis_superficie_paciente
from Functions.Services.RayosXGeneral.general_exactitud_tension_1 import general_exactitud_tension_1
from Functions.Services.RayosXGeneral.general_exactitud_tension_2 import general_exactitud_tension_2
from Functions.Services.RayosXGeneral.general_exactitud_tension_3 import general_exactitud_tension_3
from Functions.Services.RayosXGeneral.general_exactitud_tiempo_exposicion_1 import general_exactitud_tiempo_exposicion_1
from Functions.Services.RayosXGeneral.general_exactitud_tiempo_exposicion_2 import general_exactitud_tiempo_exposicion_2
from Functions.Services.RayosXGeneral.general_exactitud_tiempo_exposicion_3 import general_exactitud_tiempo_exposicion_3
from Functions.Services.RayosXGeneral.general_filtracion import general_filtracion
from Functions.Services.RayosXGeneral.general_repetibilidad_rendimiento import general_repetibilidad_rendimiento
from Functions.Services.RayosXGeneral.general_repetibilidad_tension import general_repetibilidad_tension
from Functions.Services.RayosXGeneral.general_repetibilidad_tiempo_exposicion import general_repetibilidad_tiempo_exposicion
from Functions.Services.RayosXGeneral.general_valor_rendimiento import general_valor_rendimiento
from Functions.Services.RayosXGeneral.general_variacion_rendimiento_carga import general_variacion_rendimiento_carga


class general_dosissuperficiepaciente(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_dosis_superficie_paciente(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_dosis_superficie_paciente= general_dosissuperficiepaciente.as_view()

class general_exactitudtension1(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tension_1(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tension_1= general_exactitudtension1.as_view()

class general_exactitudtension2(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tension_2(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tension_2= general_exactitudtension2.as_view()

class general_exactitudtension3(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tension_3(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tension_3= general_exactitudtension3.as_view()

class general_exactitudtiempoexposicion_1(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tiempo_exposicion_1(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tiempo_exposicion_1= general_exactitudtiempoexposicion_1.as_view()

class general_exactitudtiempoexposicion_2(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tiempo_exposicion_2(data_entrante[0],[data_entrante[1]])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tiempo_exposicion_2= general_exactitudtiempoexposicion_2.as_view()

class general_exactitudtiempoexposicion_3(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_exactitud_tiempo_exposicion_3(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_exactitud_tiempo_exposicion_3= general_exactitudtiempoexposicion_3.as_view()

class general_filtracionView(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_filtracion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_filtracion= general_filtracionView.as_view()

class general_repetibilidadrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_repetibilidad_rendimiento(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_repetibilidad_rendimiento= general_repetibilidadrendimiento.as_view()

class general_repetibilidadtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_repetibilidad_tension(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_repetibilidad_tension= general_repetibilidadtension.as_view()

class general_repetibilidadtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_repetibilidad_tiempo_exposicion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_repetibilidad_tiempo_exposicion= general_repetibilidadtiempoexposicion.as_view()

class general_valorrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_valor_rendimiento(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_valor_rendimiento= general_valorrendimiento.as_view()

class general_variacionrendimientocarga(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = general_variacion_rendimiento_carga(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_general_variacion_rendimiento_carga= general_variacionrendimientocarga.as_view()

class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status_code, 'message': 'No se encontraron registros', })
