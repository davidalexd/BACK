from django.urls import path
from . import views

urlpatterns = [
    path('Operaciones/',views.operaciones_create_view,name='operacion-list'),
    path('Operaciones/<int:pk>/',views.operaciones_list_view,name='operacion-detail'),
    path('Operaciones/<int:pk>/update/',views.operaciones_actualizar_view,name='operacion-update'),
    path('Operaciones/<int:pk>/delete/',views.operaciones_eliminar_view,name='operacion-delete'),
]