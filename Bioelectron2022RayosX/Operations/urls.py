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
    path('OperacionFluoroscopiaDistorsionIntegral/<global>',views.view_fluoroscopia_distorsion_integral,name='fluoroscopia_distorsion_integral'),
    path('OperacionFluoroscopiaDistorsionTipoS/<global>',views.view_fluoroscopia_distorsion_del_tipo_s,name='fluoroscopia_distorsion_del_tipo_s'),
    path('OperacionFluoroscopiaDistorsionCojinete/<global>',views.view_fluoroscopia_distorsion_cojinete,name='fluoroscopia_distorsion_cojinete'),
    
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
    path('OperacionFluoroscopiafResolucionEspacialAltoContrastecontraste/<global>',views.view_fluoroscopia_resolucion_espacial_alto_contraste,name="fluoroscopia_resolucion_espacial_alto_contraste"),
    path('OperacionFluoroscopiaCompensacionCae/<global>',views.view_fluoroscopia_compensacion_cae,name="fluoroscopia_compensacion_cae"),
    path('OperacionFluoroscopiaCompensacionDiferentesEspesores/<global>',views.view_fluoroscopia_compensacion_diferentes_espesores,name="fluoroscopia_compensacion_diferentes_espesores"),
    path('OperacionFluoroscopiaKermaAireEntradaPaciente/<global>',views.view_fluoroscopia_kerma_aire_entrada_paciente,name="fluoroscopia_kerma_aire_entrada_paciente"),
    path('OperacionFluoroscopiaRepetibilidadCae/<global>',views.view_fluoroscopia_repetibilidad_cae,name="fluoroscopia_repetibilidad_cae"),
    path('OperacionFluoroscopiaRepetibilidadCai/<global>',views.view_fluoroscopia_repetibilidad_cai,name="fluoroscopia_repetibilidad_cai"),
    path('OperacionFluoroscopiaTasaDosisMaximaEntradaIntensificacionImagen/<global>',views.view_fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen,name="fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen"),
    path('OperacionFluoroscopiaTasaDosisPaciente/<global>',views.view_fluoroscopia_tasa_dosis_paciente,name="fluoroscopia_tasa_dosis_paciente"),
    path('OperacionFluoroscopiaUmbralSensibilidadBajoContraste/<global>',views.view_fluoroscopia_umbral_sensibilidad_bajo_contraste,name="fluoroscopia_umbral_sensibilidad_bajo_contraste"),

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
    path('OperacionGeneralAlineaciónRayosXHazLuminoso/<global>',views.view_general_alineación_rayos_X_haz_luminoso,name='general_alineación_rayos_X_haz_luminoso'),
    path('OperacionGeneralOrtogonalidadHazRayosXReceptorImagen/<global>',views.view_general_ortogonalidad_haz_rayos_X_receptor_imagen,name='general_ortogonalidad_haz_rayos_X_receptor_imagen'),
    path('OperacionGeneralRepetibilidadCae/<global>',views.view_general_repetibilidad_cae,name='general_repetibilidad_cae'),
    path('OperacionGeneralRepetibilidadCae1/<global>',views.view_general_repetibilidad_cae_1,name='general_repetibilidad_cae_1'),
    path('OperacionGeneralRepetibilidadCae2/<global>',views.view_general_repetibilidad_cae_2,name='general_repetibilidad_cae_2'),

    path('OperacionTomografiaCoincidenciaindicadoresluminososplanoexternointernoirradiado/<global>',views.view_tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado,name='tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado'),
    path('OperacionTomografiaExactitudincrementodesplazamientodemesa/<global>',views.view_tomografia_exactitud_incremento_desplazamiento_de_mesa,name='tomografia_exactitud_incremento_desplazamiento_de_mesa'),
    path('OperacionTomografiaExactitudindicadorposicionmesa/<global>',views.view_tomografia_exactitud_indicador_posicion_mesa,name='tomografia_exactitud_indicador_posicion_mesa'),
    path('OperacionTomografiaExactitudtension/<global>',views.view_tomografia_exactitud_tension,name='tomografia_exactitud_tension'),
    path('OperacionTomografiaExploracionparaabdomen/<global>',views.view_tomografia_exploracion_para_abdomen,name='tomografia_exploracion_para_abdomen'),
    path('OperacionTomografiaExploracionparacabeza/<global>',views.view_tomografia_exploracion_para_cabeza,name='tomografia_exploracion_para_cabeza'),
    path('OperacionTomografiaFiltracioncapahemirreductora/<global>',views.view_tomografia_filtracion_capa_hemirreductora,name='tomografia_filtracion_capa_hemirreductora'),
    path('OperacionTomografiaPerfilessensibilidad/<global>',views.view_tomografia_perfiles_sensibilidad,name='tomografia_perfiles_sensibilidad'),
    path('OperacionTomografiaRepetibilidadrendimiento/<global>',views.view_tomografia_repetibilidad_rendimiento,name='tomografia_repetibilidad_rendimiento'),
    path('OperacionTomografiaRepetibilidadtension/<global>',views.view_tomografia_repetibilidad_tension,name='tomografia_repetibilidad_tension'),
    path('OperacionTomografiaRuidoimagen/<global>',views.view_tomografia_ruido_imagen,name='tomografia_ruido_imagen'),
    path('OperacionTomografiaUniformidadespacialnumeroct/<global>',views.view_tomografia_uniformidad_espacial_numero_ct,name='tomografia_uniformidad_espacial_numero_ct'),
    path('OperacionTomografiaValormedionumeroct/<global>',views.view_tomografia_valor_medio_numero_ct,name='tomografia_valor_medio_numero_ct'),
    path('OperacionTomografiaVariacionrendimientocarga/<global>',views.view_tomografia_variacion_rendimiento_carga,name='tomografia_variacion_rendimiento_carga'),
    path('OperacionTomografiaVerificacionausenciaartefactosimagen/<global>',views.view_tomografia_verificacion_ausencia_artefactos_imagen,name='tomografia_verificacion_ausencia_artefactos_imagen'),
    path('OperacionTomografiaExactitudseleccionposicioncorteradiografiaplanificacion/<global>',views.view_tomografia_exactitud_seleccion_posicion_corte_radiografia_planificacion,name='tomografia_exactitud_seleccion_posicion_corte_radiografia_planificacion'),

    path('OperacionMamografiaDistanciaFocoPelículaDetectorImagen/<global>',views.view_mamografia_distancia_foco_película_detector_imagen,name='mamografia_distancia_foco_película_detector_imagen'),
    path('OperacionMamografiaCoincidenciaCampoRadiacionReceptorImagen/<global>',views.view_mamografia_coincidencia_campo_radiacion_receptor_imagen,name='mamografia_coincidencia_campo_radiacion_receptor_imagen'),
    path('OperacionMamografiaExactitudTension/<global>',views.view_mamografia_exactitud_tension,name='mamografia_exactitud_tension'),
    path('OperacionMamografiaRepetibilidadTension/<global>',views.view_mamografia_repetibilidad_tension,name='mamografia_repetibilidad_tension'),   
    path('OperacionMamografiaFiltracionCapaHemirreductora/<global>',views.view_mamografia_filtracion_capa_hemirreductora,name='mamografia_filtracion_capa_hemirreductora'),   
    path('OperacionMamografiaExactitudTiempoExposicion/<global>',views.view_mamografia_exactitud_tiempo_exposicion,name='mamografia_exactitud_tiempo_exposicion'),   
    path('OperacionMamografiaRepitibilidadTiempoExposicion/<global>',views.view_mamografia_repetibilidad_tiempo_exposicion,name='mamografia_repetibilidad_tiempo_exposicion'),   
    path('OperacionMamografiaRepetibilidadCAE/<global>',views.view_mamografia_repetibilidad_cae,name='mamografia_repetibilidad_cae'),   
    path('OperacionMamografiaCompensacionCAE/<global>',views.view_mamografia_compensacion_cae_espesor_composición_mama,name='mamografia_compensacion_cae_espesor_composición_mama'),   
    path('OperacionMamografiaRepetibilidadRendimiento/<global>',views.view_mamografia_repetibilidad_rendimiento,name='mamografia_repetibilidad_rendimiento'),   
    path('OperacionMamografiaLinealidadRendimientoCargaTubo/<global>',views.view_mamografia_linealidad_rendimiento_carga_tubo,name='mamografia_linealidad_rendimiento_carga_tubo'),   
    path('OperacionMamografiaFuerzaComprensionAtenuacionCompresor/<global>',views.view_mamografia_fuerza_compresion_atenuacion_compresor,name='mamografia_fuerza_compresion_atenuacion_compresor'),   
    path('OperacionMamografiaExactitudFuerzaCompresion/<global>',views.view_mamografia_exactitud_fuerza_compresion,name='mamografia_exactitud_fuerza_compresion'),   
    path('OperacionMamografiaResolucionEspacial/<global>',views.view_mamografia_resolucion_espacial,name='mamografia_resolucion_espacial'),   
    path('OperacionMamografiaVisibilidadPequenosObjetosMicrocalcificaciones/<global>',views.view_mamografia_visibilidad_pequenos_objetos_microcalcificaciones,name='mamografia_visibilidad_pequenos_objetos_microcalcificaciones'),   
    path('OperacionMamografiaPerdidaImagenParedTorax/<global>',views.view_mamografia_perdida_imagen_pared_torax,name='mamografia_perdida_imagen_pared_torax'),   
    path('OperacionMamografiaUniformidadImagen/<global>',views.view_mamografia_uniformidad_imagen,name='mamografia_uniformidad_imagen'),   
    path('OperacionMamografiaArtefactosCr/<global>',views.view_mamografia_artefactos_cr,name='mamografia_artefactos_cr'),   
    path('OperacionMamografiaArtefactosVerificacionElementosDefectuososDetectorDr/<global>',views.view_mamografia_artefactos_verificacion_elementos_defectuosos_detector_dr,name='mamografia_artefactos_verificacion_elementos_defectuosos_detector_dr'),   
    path('OperacionMamografiaDosisSuperficieMama/<global>',views.view_mamografia_dosis_superficie_mama,name='mamografia_dosis_superficie_mama'),   
    
    
    path('OperacionDentalPanoramicoAlineamientoReceptorImagen/<global>',views.view_dental_panoramico_alineamiento_receptor_imagen,name='dental_panoramico_alineamiento_receptor_imagen'),
    path('OperacionDentalPanoramicoCfalometrico2/<global>',views.view_dental_panoramico_cfalometrico_2,name='dental_panoramico_cfalometrico_2'),
    path('OperacionDentalPanoramicoCfalometrico/<global>',views.view_dental_panoramico_cfalometrico,name='dental_panoramico_cfalometrico'),
    path('OperacionDentalPanoramicoExactitudTension/<global>',views.view_dental_panoramico_exactitud_tension,name='dental_panoramico_exactitud_tension'),
    path('OperacionDentalPanoramicoFiltracion/<global>',views.view_dental_panoramico_filtracion,name='dental_panoramico_filtracion'),
    path('OperacionDentalPanoramicoPanoramico2/<global>',views.view_dental_panoramico_panoramico_2,name='dental_panoramico_panoramico_2'),
    path('OperacionDentalPanoramicoPanoramico/<global>',views.view_dental_panoramico_panoramico,name='dental_panoramico_panoramico'),
    path('OperacionDentalPanoramicoRepetibilidadRendimiento/<global>',views.view_dental_panoramico_repetibilidad_rendimiento,name='dental_panoramico_repetibilidad_rendimiento'),
    path('OperacionDentalPanoramicoRepetibilidadTension/<global>',views.view_dental_panoramico_repetibilidad_tension,name='dental_panoramico_repetibilidad_tension'),
    path('OperacionDentalPanoramicoTamanoCampoRadicacion/<global>',views.view_dental_panoramico_tamano_campo_radiacion,name='dental_panoramico_tamano_campo_radiacion'),
    path('OperacionDentalPanoramicoValorRendimiento/<global>',views.view_dental_panoramico_valor_rendimiento,name='dental_panoramico_valor_rendimiento'),
    path('OperacionDentalPanoramicoVariacionRendimiento/<global>',views.view_dental_panoramico_variacion_rendimiento,name='dental_panoramico_variacion_rendimiento'),
    
]