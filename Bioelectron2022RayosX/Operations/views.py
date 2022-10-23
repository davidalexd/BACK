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
from Functions.Services.RayosXFluoroscopia.fluoroscopia_exactitud_tiempo_exposicion import fluoroscopia_exactitud_tiempo_exposicion
from Functions.Services.RayosXFluoroscopia.fluoroscopia_filtracion_capa_hemireductora import fluoroscopia_filtracion_capa_hemireductora
from Functions.Services.RayosXFluoroscopia.fluoroscopia_repetibilidad_tension import fluoroscopia_repetibilidad_tension
from Functions.Services.RayosXFluoroscopia.fluoroscopia_exactitud_tension import fluoroscopia_exactitud_tension
from Functions.Services.RayosXFluoroscopia.fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector import fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector
from Functions.Services.RayosXFluoroscopia.fluoroscopia_tamano_campo_entrada_detector_imagen import fluoroscopia_tamano_campo_entrada_detector_imagen
from Functions.Services.RayosXFluoroscopia.fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen import fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen

from Functions.Services.RayosXFluoroscopia.fluoroscopia_distorsion_geometrica import fluoroscopia_distorsion_integral
from Functions.Services.RayosXFluoroscopia.fluoroscopia_distorsion_geometrica import fluoroscopia_distorsion_del_tipo_s
from Functions.Services.RayosXFluoroscopia.fluoroscopia_distorsion_geometrica import fluoroscopia_distorsion_cojinete

from Functions.Services.RayosXFluoroscopia.fluoroscopia_alineacion_rayos_x_haz_luminoso import fluoroscopia_alineacion_rayos_x_haz_luminoso
from Functions.Services.RayosXFluoroscopia.fluoroscopia_repetibilidad_tiempo_exposicion import fluoroscopia_repetibilidad_tiempo_exposicion
from Functions.Services.RayosXFluoroscopia.fluoroscopia_repetibilidad_rendimiento import fluoroscopia_repetibilidad_rendimiento
from Functions.Services.RayosXFluoroscopia.fluoroscopia_valor_rendimiento import fluoroscopia_valor_rendimiento
from Functions.Services.RayosXFluoroscopia.fluoroscopia_variacion_rendimiento_carga import fluoroscopia_variacion_rendimiento_carga
from Functions.Services.RayosXFluoroscopia.fluoroscopia_resolucion_espacial_alto_contraste import fluoroscopia_resolucion_espacial_alto_contraste
from Functions.Services.RayosXFluoroscopia.fluoroscopia_compensacion_cae import fluoroscopia_compensacion_cae
from Functions.Services.RayosXFluoroscopia.fluoroscopia_compensacion_diferentes_espesores import fluoroscopia_compensacion_diferentes_espesores
from Functions.Services.RayosXFluoroscopia.fluoroscopia_kerma_aire_entrada_paciente import fluoroscopia_kerma_aire_entrada_paciente
from Functions.Services.RayosXFluoroscopia.fluoroscopia_repetibilidad_cae import fluoroscopia_repetibilidad_cae
from Functions.Services.RayosXFluoroscopia.fluoroscopia_repetibilidad_cai import fluoroscopia_repetibilidad_cai
from Functions.Services.RayosXFluoroscopia.fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen import fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen
from Functions.Services.RayosXFluoroscopia.fluoroscopia_tasa_dosis_paciente import fluoroscopia_tasa_dosis_paciente
from Functions.Services.RayosXFluoroscopia.fluoroscopia_umbral_sensibilidad_bajo_contraste import fluoroscopia_umbral_sensibilidad_bajo_contraste

class fluoroscopia_alineacionrayosxhazluminoso(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_alineacion_rayos_x_haz_luminoso((data_entrante[0]),(data_entrante[1]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_alineacion_rayos_x_haz_luminoso = fluoroscopia_alineacionrayosxhazluminoso.as_view()

class fluoroscopia_distorsionintegral(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_distorsion_integral((data_entrante[0]),(data_entrante[1]),(data_entrante[2]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_fluoroscopia_distorsion_integral = fluoroscopia_distorsionintegral.as_view()
class fluoroscopia_distorsiondeltipos(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_distorsion_del_tipo_s((data_entrante[0]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_fluoroscopia_distorsion_del_tipo_s = fluoroscopia_distorsiondeltipos.as_view()
class fluoroscopia_distorsioncojinete(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_distorsion_cojinete((data_entrante[0]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_fluoroscopia_distorsion_cojinete = fluoroscopia_distorsioncojinete.as_view()




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
            resultado = fluoroscopia_exactitud_tension((data_entrante[0]),(data_entrante[1]),(data_entrante[2]),(data_entrante[3]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_exactitud_tension = fluoroscopia_exactitudtension.as_view()

class fluoroscopia_repetibilidadtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_tension((data_entrante[0]),(data_entrante[1]),(data_entrante[2]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_tension = fluoroscopia_repetibilidadtension.as_view()

class fluoroscopia_filtracioncapahemireductora(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_filtracion_capa_hemireductora(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_filtracion_capa_hemireductora = fluoroscopia_filtracioncapahemireductora.as_view()

class fluoroscopia_exactitudtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_exactitud_tiempo_exposicion((data_entrante[0]),(data_entrante[1]),(data_entrante[2]),(data_entrante[3]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_exactitud_tiempo_exposicion = fluoroscopia_exactitudtiempoexposicion.as_view()

class fluoroscopia_repetibilidadtiempoexposicion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_tiempo_exposicion((data_entrante[0]),(data_entrante[1]),(data_entrante[2]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_tiempo_exposicion = fluoroscopia_repetibilidadtiempoexposicion.as_view()

class fluoroscopia_valorrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_valor_rendimiento(data_entrante[0],(data_entrante[1]),(data_entrante[2]),(data_entrante[3]),(data_entrante[4]))
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_valor_rendimiento = fluoroscopia_valorrendimiento.as_view()

class fluoroscopia_repetibilidadrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = fluoroscopia_repetibilidad_rendimiento(data_entrante[0],data_entrante[1],data_entrante[2])
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

class fluoroscopia_resolucionespacialaltocontraste(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_resolucion_espacial_alto_contraste(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_resolucion_espacial_alto_contraste = fluoroscopia_resolucionespacialaltocontraste.as_view()

class fluoroscopia_compensacioncae(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_compensacion_cae(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_compensacion_cae = fluoroscopia_compensacioncae.as_view()

class fluoroscopia_compensaciondiferentesespesores(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_compensacion_diferentes_espesores(data_entrante[0],data_entrante[1],data_entrante[12],data_entrante[3])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_compensacion_diferentes_espesores = fluoroscopia_compensaciondiferentesespesores.as_view()

class fluoroscopia_kermaaireentradapaciente(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_kerma_aire_entrada_paciente(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3],data_entrante[4])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_kerma_aire_entrada_paciente = fluoroscopia_kermaaireentradapaciente.as_view()

class fluoroscopia_repetibilidadcae(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_repetibilidad_cae(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_cae = fluoroscopia_repetibilidadcae.as_view()

class fluoroscopia_repetibilidadcai(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_repetibilidad_cai(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_repetibilidad_cai = fluoroscopia_repetibilidadcai.as_view()

class fluoroscopia_tasadosismaximaentradaintensificadorimagen(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen = fluoroscopia_tasadosismaximaentradaintensificadorimagen.as_view()

class fluoroscopia_tasadosispaciente(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_tasa_dosis_paciente(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_tasa_dosis_paciente = fluoroscopia_tasadosispaciente.as_view()

class fluoroscopia_umbralsensibilidadbajocontraste(View):
    def get(self,request,**kwargs):
        try:
            data_entrante = json.loads(kwargs["global"])
            resultado = fluoroscopia_umbral_sensibilidad_bajo_contraste(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})
view_fluoroscopia_umbral_sensibilidad_bajo_contraste = fluoroscopia_umbralsensibilidadbajocontraste.as_view()



# dental
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


# General
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


from Functions.Services.RayosXTomografia.tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado import tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado
from Functions.Services.RayosXTomografia.tomografia_exactitud_incremento_desplazamiento_de_mesa import tomografia_exactitud_incremento_desplazamiento_de_mesa
from Functions.Services.RayosXTomografia.tomografia_exactitud_indicador_posicion_mesa import tomografia_exactitud_indicador_posicion_mesa
from Functions.Services.RayosXTomografia.tomografia_exactitud_tension import tomografia_exactitud_tension
from Functions.Services.RayosXTomografia.tomografia_exploracion_para_abdomen import tomografia_exploracion_para_abdomen
from Functions.Services.RayosXTomografia.tomografia_exploracion_para_cabeza import tomografia_exploracion_para_cabeza
from Functions.Services.RayosXTomografia.tomografia_filtracion_capa_hemirreductora import tomografia_filtracion_capa_hemirreductora
from Functions.Services.RayosXTomografia.tomografia_perfiles_sensibilidad import tomografia_perfiles_sensibilidad
from Functions.Services.RayosXTomografia.tomografia_repetibilidad_rendimiento import tomografia_repetibilidad_rendimiento
from Functions.Services.RayosXTomografia.tomografia_repetibilidad_tension import tomografia_repetibilidad_tension
from Functions.Services.RayosXTomografia.tomografia_ruido_imagen import tomografia_ruido_imagen
from Functions.Services.RayosXTomografia.tomografia_uniformidad_espacial_numero_ct import tomografia_uniformidad_espacial_numero_ct
from Functions.Services.RayosXTomografia.tomografia_valor_medio_numero_ct import tomografia_valor_medio_numero_ct
from Functions.Services.RayosXTomografia.tomografia_variacion_rendimiento_carga import tomografia_variacion_rendimiento_carga
from Functions.Services.RayosXTomografia.tomografia_verificacion_ausencia_artefactos_imagen import tomografia_verificacion_ausencia_artefactos_imagen
from Functions.Services.RayosXTomografia.tomografia_exactitud_seleccion_posicion_corte_radiografia_planificacion import tomograifa_exactitud_seleccion_posicion_corte_radiografia_planificacion


class tomografia_coincidenciaindicadoresluminososplanoexternointernoirradiado(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado = tomografia_coincidenciaindicadoresluminososplanoexternointernoirradiado.as_view()
class tomografia_exactitudincrementodesplazamientodemesa(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_exactitud_incremento_desplazamiento_de_mesa(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exactitud_incremento_desplazamiento_de_mesa = tomografia_exactitudincrementodesplazamientodemesa.as_view()
class tomografia_exactitudindicadorposicionmesa(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_exactitud_indicador_posicion_mesa(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exactitud_indicador_posicion_mesa = tomografia_exactitudindicadorposicionmesa.as_view()
class tomografia_exactitudtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_exactitud_tension(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exactitud_tension = tomografia_exactitudtension.as_view()
class tomografia_exploracionparaabdomen(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_exploracion_para_abdomen(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3],data_entrante[4],data_entrante[5],data_entrante[6],data_entrante[7],data_entrante[8],data_entrante[9],data_entrante[10],data_entrante[11],data_entrante[12])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exploracion_para_abdomen = tomografia_exploracionparaabdomen.as_view()
class tomografia_exploracionparacabeza(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_exploracion_para_cabeza(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3],data_entrante[4],data_entrante[5],data_entrante[6],data_entrante[7],data_entrante[8],data_entrante[9],data_entrante[10],data_entrante[11],data_entrante[12])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exploracion_para_cabeza = tomografia_exploracionparacabeza.as_view()
class tomografia_filtracioncapahemirreductora(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_filtracion_capa_hemirreductora(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_filtracion_capa_hemirreductora = tomografia_filtracioncapahemirreductora.as_view()
class tomografia_perfilessensibilidad(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_perfiles_sensibilidad(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_perfiles_sensibilidad = tomografia_perfilessensibilidad.as_view()
class tomografia_repetibilidadrendimiento(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_repetibilidad_rendimiento(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_repetibilidad_rendimiento = tomografia_repetibilidadrendimiento.as_view()
class tomografia_repetibilidadtension(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_repetibilidad_tension(data_entrante[0],data_entrante[1],data_entrante[2])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_repetibilidad_tension = tomografia_repetibilidadtension.as_view()
class tomografia_ruidoimagen(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_ruido_imagen(data_entrante[0],data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_ruido_imagen = tomografia_ruidoimagen.as_view()
class tomografia_uniformidadespacialnumeroct(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_uniformidad_espacial_numero_ct(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_uniformidad_espacial_numero_ct = tomografia_uniformidadespacialnumeroct.as_view()
class tomografia_valormedionumeroct(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_valor_medio_numero_ct(data_entrante[0],data_entrante[1])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_valor_medio_numero_ct = tomografia_valormedionumeroct.as_view()
class tomografia_variacionrendimientocarga(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_variacion_rendimiento_carga(data_entrante[0],data_entrante[1],data_entrante[2],data_entrante[3],data_entrante[4])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_variacion_rendimiento_carga = tomografia_variacionrendimientocarga.as_view()
class tomografia_verificacionausenciaartefactosimagen(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomografia_verificacion_ausencia_artefactos_imagen(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_verificacion_ausencia_artefactos_imagen = tomografia_verificacionausenciaartefactosimagen.as_view()
class tomografia_exactitudseleccionposicioncorteradiografiaplanificacion(View):
    def get(self, request,**kwargs):
        try:
            data_entrante = json.loads(kwargs['global'])
            resultado = tomograifa_exactitud_seleccion_posicion_corte_radiografia_planificacion(data_entrante[0])
            return JsonResponse({'resultado':resultado}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({ 'response_code': '404', 'response': status.HTTP_404_NOT_FOUND, 'message': 'Proporcionar valores válidos para la operación'})

view_tomografia_exactitud_seleccion_posicion_corte_radiografia_planificacion = tomografia_exactitudseleccionposicioncorteradiografiaplanificacion.as_view()

class ValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = ({ 'response_code': '404', 'response': status_code, 'message': 'No se encontraron registros', })
