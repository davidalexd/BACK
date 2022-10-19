from django.urls import path
from . import views

urlpatterns = [
    path('Operaciones/',views.operaciones_create_view,name='operacion-list'),
    path('Operaciones/<int:pk>/',views.operaciones_list_view,name='operacion-detail'),
    path('Operaciones/<int:pk>/update/',views.operaciones_actualizar_view,name='operacion-update'),
    path('Operaciones/<int:pk>/delete/',views.operaciones_eliminar_view,name='operacion-delete'),

    path('Variables/',views.variables_create_view,name='variable-list'),
    path('Variables/<int:pk>/',views.variables_list_view,name='variable-detail'),
    path('Variables/<int:pk>/update/',views.variables_actualizar_view,name='variable-update'),
    path('Variables/<int:pk>/delete/',views.variables_eliminar_view,name='variable-delete'),

    path('CateogriaOperaciones/',views.categoria_operaciones_create_view,name='categoria-operacion-list'),
    path('CateogriaOperaciones/<int:pk>/',views.categoria_operaciones_list_view,name='categoria-operacion-detail'),
    path('CateogriaOperaciones/<int:pk>/update/',views.categoria_operaciones_actualizar_view,name='categoria-operacion-update'),
    path('CateogriaOperaciones/<int:pk>/delete/',views.categoria_operaciones_eliminar_view,name='categoria-operacion-delete'),

    path('OperacionFluoroscopiaAlineacionRayosXHazLuminoso/<global>',views.view_fluoroscopia_alineacion_rayos_x_haz_luminoso,name='fluoroscopia_alineacion_rayos_x_haz_luminoso'),
    path('OperacionFluoroscopiaDistorsionGeometrica/<global>',views.view_fluoroscopia_distorsion_geometrica,name='fluoroscopia_distorsion_geometrica'),
    path('OperacionFluoroscopiaOrtogonalidadHazRayosXReceptorImagen/<global>',views.view_fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen,name='fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen'),
    path('OperacionFluoroscopiaTamanoCampoEntradaDetectorImagen/<global>',views.view_fluoroscopia_tamano_campo_entrada_detector_imagen,name='fluoroscopia_tamano_campo_entrada_detector_imagen'),
    path('OperacionFluoroscopiaCoincidenciaCampoRadiacionAreaVisualizadaDetector/<global>',views.view_fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector,name='fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector'),
    path('OperacionFluoroscopiaExactitudTension/<global>',views.view_fluoroscopia_exactitud_tension,name='fluoroscopia_exactitud_tension'),
    path('OperacionFluoroscopiaRepetibilidadTension/<global>',views.view_fluoroscopia_repetibilidad_tension,name='fluoroscopia_repetibilidad_tension'),
    path('OperacionFluoroscopiaFiltracionCapaHemireductora/<global>',views.view_fluoroscopia_filtracion_capa_hemireductora,name='fluoroscopia_filtracion_capa_hemireductora'),
    path('OperacionFluoroscopiaExactitudTiempoExposicion/<global>',views.view_fluoroscopia_exactitud_tiempo_exposicion,name='fluoroscopia_exactitud_tiempo_exposicion'),
    path('OperacionFluoroscopiaRepetibilidadTiempoExposicion/<global>',views.view_fluoroscopia_repetibilidad_tiempo_exposicion,name='fluoroscopia_repetibilidad_tiempo_exposicion'),
    path('OperacionFluoroscopiaValorRendimiento/<global>',views.view_fluoroscopia_valor_rendimiento,name='fluoroscopia_valor_rendimiento'),
    path('OperacionFluoroscopiaRepetibilidadRendimiento/<global>',views.view_fluoroscopia_repetibilidad_rendimiento,name='fluoroscopia_repetibilidad_rendimiento'),
    path('OperacionFluoroscopiaVariacionRendimientoCarga/<global>',views.view_fluoroscopia_variacion_rendimiento_carga,name='fluoroscopia_variacion_rendimiento_carga'),


    path('OperacionDentalExactitudTension/<global>',views.view_dental_exactitud_tension,name='dental_exactitud_tension'),
    path('OperacionDentalExactitudTiempoTexposicion_1/<global>',views.view_dental_exactitud_tiempo_exposicion_1,name='dental_exactitud_tiempo_exposicion_1'),
    path('OperacionDentalExactitudTiempoTexposicion_2/<global>',views.view_dental_exactitud_tiempo_exposicion_2,name='dental_exactitud_tiempo_exposicion_2'),
    path('OperacionDentalFiltracion/<global>',views.view_dental_filtracion,name='dental_filtracion'),
    path('OperacionDentalKermaAireEntradaPaciente/<global>',views.view_dental_kerma_aire_entrada_paciente,name='dental_kerma_aire_entrada_paciente'),
    path('OperacionDentalMinimaDistanciaFocoPiel/<global>',views.view_dental_minima_distancia_foco_piel,name='dental_minima_distancia_foco_piel'),
    path('OperacionDentalRepetibilidadRendimiento/<global>',views.view_dental_repetibilidad_rendimiento,name='dental_repetibilidad_rendimiento'),
    path('OperacionDentaRepetibilidadTensionl/<global>',views.view_dental_repetibilidad_tension,name='dental_repetibilidad_tension'),
    path('OperacionDentalRepetibilidadTiempoExposicion/<global>',views.view_dental_repetibilidad_tiempo_exposicion,name='dental_repetibilidad_tiempo_exposicion'),
    path('OperacionDentalTamanoCampoExtremoLocalizador/<global>',views.view_dental_tamano_campo_extremo_localizador,name='dental_tamano_campo_extremo_localizador'),
    path('OperacionDentalValorRendimiento/<global>',views.view_dental_valor_rendimiento,name='dental_valor_rendimiento'),
    path('OperacionDentalVriacionRendimiento/<global>',views.view_dental_variacion_rendimiento,name='dental_variacion_rendimiento'),

    path('OperacionGeneralDosisSuperficiePaciente/<global>',views.view_general_dosis_superficie_paciente,name='general_dosis_superficie_paciente'),
    path('OperacionGeneralExactitudTension_1/<global>',views.view_general_exactitud_tension_1,name='general_exactitud_tension_1'),
    path('OperacionGeneralExactitudTension_2/<global>',views.view_general_exactitud_tension_2,name='general_exactitud_tension_2'),
    path('OperacionGeneralExactitudTension_3/<global>',views.view_general_exactitud_tension_3,name='general_exactitud_tension_3'),
    path('OperacionGeneralExactitudTiempoExposicion_1/<global>',views.view_general_exactitud_tiempo_exposicion_1,name='general_exactitud_tiempo_exposicion_1'),
    path('OperacionGeneralExactitudTiempoExposicion_2/<global>',views.view_general_exactitud_tiempo_exposicion_2,name='general_exactitud_tiempo_exposicion_2'),
    path('OperacionGeneralExactitudTiempoExposicion_3/<global>',views.view_general_exactitud_tiempo_exposicion_3,name='general_exactitud_tiempo_exposicion_3'),
    path('OperacionGeneralFiltracion/<global>',views.view_general_filtracion,name='general_filtracion'),
    path('OperacionGeneralRepetibilidadRendimiento/<global>',views.view_general_repetibilidad_rendimiento,name='general_repetibilidad_rendimiento'),
    path('OperacionGeneralRepetibilidadTension/<global>',views.view_general_repetibilidad_tension,name='general_repetibilidad_tension'),
    path('OperacionGeneralRepetibilidadTiempoExposicion/<global>',views.view_general_repetibilidad_tiempo_exposicion,name='general_repetibilidad_tiempo_exposicion'),
    path('OperacionGeneralValorRendimiento/<global>',views.view_general_valor_rendimiento,name='general_valor_rendimiento'),
    path('OperacionGeneralVariacionRendimientoCarga/<global>',views.view_general_variacion_rendimiento_carga,name='general_variacion_rendimiento_carga'),



]