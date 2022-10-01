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

    path('AreasHistory/',views.areas_history_view,name='area-history-list'),
    path('DepartamentosHistory/',views.departamento_history_view,name='departamento-history-detail'),
    path('OrganizacionesHistory/',views.organizacion_history_view,name='organizacion-history-update'), 
]