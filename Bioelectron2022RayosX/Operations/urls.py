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
]