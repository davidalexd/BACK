from django.urls import path
from . import views

urlpatterns = [
    path('Organizaciones/',views.organzizaciones_create_view,name='organizacion-list'),
    path('Organizaciones/<int:pk>/',views.organzizaciones_list_view,name='organizacion-detail'),
    path('Organizaciones/<int:pk>/update/',views.organzizaciones_actualizar_view,name='organizacion-update'),
    path('Organizaciones/<int:pk>/delete/',views.organzizaciones_eliminar_view,name='organizacion-delete')
]