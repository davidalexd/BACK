from django.urls import path
from . import views

urlpatterns = [
    path('Protocolos/',views.protocolos_create_view,name='protocolo-list'),
    path('Protocolos/<int:pk>/',views.protocolos_list_view,name='protocolo-detail'),
    path('Protocolos/<int:pk>/update/',views.protocolos_actualizar_view,name='protocolo-update'),
    path('Protocolos/<int:pk>/delete/',views.protocolos_eliminar_view,name='protocolo-delete'),

    path('Secciones/',views.secciones_create_view,name='seccion-list'),
    path('Secciones/<int:pk>/',views.secciones_list_view,name='seccion-detail'),
    path('Secciones/<int:pk>/update/',views.secciones_actualizar_view,name='seccion-update'),
    path('Secciones/<int:pk>/delete/',views.secciones_eliminar_view,name='seccion-delete'),

    path('PruebasCalculo/',views.prueba_calculo_create_view,name='prueba-calculo-list'),
    path('PruebasCalculo/<int:pk>/',views.prueba_calculo_list_view,name='prueba-calculo-detail'),
    path('PruebasCalculo/<int:pk>/update/',views.prueba_calculo_actualizar_view,name='prueba-calculo-update'),
    path('PruebasCalculo/<int:pk>/delete/',views.prueba_calculo_eliminar_view,name='prueba-calculo-delete'),

    path('PruebasOpcion/',views.pruebas_opciones_create_view,name='prueba-opcion-list'),
    path('PruebasOpcion/<int:pk>/',views.pruebas_opciones_list_view,name='prueba-opcion-detail'),
    path('PruebasOpcion/<int:pk>/update/',views.pruebas_opciones_actualizar_view,name='prueba-opcion-update'),
    path('PruebasOpcion/<int:pk>/delete/',views.pruebas_opciones_eliminar_view,name='prueba-opcion-delete'),

]