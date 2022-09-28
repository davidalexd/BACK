from django.urls import path
from . import views

urlpatterns = [
    path('Organizaciones/',views.organzizaciones_create_view,name='organizacion-list'),
    path('Organizaciones/<int:pk>/',views.organzizaciones_list_view,name='organizacion-detail'),
    path('Organizaciones/<int:pk>/update/',views.organzizaciones_actualizar_view,name='organizacion-update'),
    path('Organizaciones/<int:pk>/delete/',views.organzizaciones_eliminar_view,name='organizacion-delete'),

    path('Departamentos/',views.departamentos_create_view,name='departamento-list'),
    path('Departamentos/<int:pk>/',views.departamentos_list_view,name='departamento-detail'),
    path('Departamentos/<int:pk>/update/',views.departamentos_actualizar_view,name='departamento-update'),
    path('Departamentos/<int:pk>/delete/',views.departamentos_eliminar_view,name='departamento-delete'),

    path('Areas/',views.areas_create_view,name='area-list'),
    path('Areas/<int:pk>/',views.areas_list_view,name='area-detail'),
    path('Areas/<int:pk>/update/',views.areas_actualizar_view,name='area-update'),
    path('Areas/<int:pk>/delete/',views.areas_eliminar_view,name='area-delete'),  

    
    path('Contactos/',views.contactos_create_view,name='contacto-list'),
    path('Contactos/<int:pk>/',views.contactos_list_view,name='contacto-detail'),
    path('Contactos/<int:pk>/update/',views.contactos_actualizar_view,name='contacto-update'),
    path('Contactos/<int:pk>/delete/',views.contactos_eliminar_view,name='contacto-delete'),  

    path('AreasHistory/',views.areas_history_view,name='area-history-list'),
    path('DepartamentosHistory/',views.departamento_history_view,name='departamento-history-list'),
    path('OrganizacionesHistory/',views.organizacion_history_view,name='organizacion-history-list'), 
    path('ContactosHistory/',views.contactos_history_view,name='contactos-history-list'), 
]