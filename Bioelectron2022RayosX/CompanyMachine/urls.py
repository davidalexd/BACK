from django.urls import path
from . import views

urlpatterns = [
    path('Calibraciones/',views.calibraciones_create_view,name='calibracion-list'),
    path('Calibraciones/<int:pk>/',views.calibraciones_list_view,name='calibracion-detail'),
    path('Calibraciones/<int:pk>/update/',views.calibraciones_actualizar_view,name='calibracion-update'),
    path('Calibraciones/<int:pk>/delete/',views.calibraciones_eliminar_view,name='calibracion-delete'),

    path('Medidores/',views.medidores_create_view,name='medidor-list'),
    path('Medidores/<int:pk>/',views.medidores_list_view,name='medidor-detail'),
    path('MedidoresMultiples/<pk>/',views.medidores_list_multiple_view,name='medidor-detail-multiple'),
    path('Medidores/<int:pk>/update/',views.medidores_actualizar_view,name='medidor-update'),
    path('Medidores/<int:pk>/delete/',views.medidores_eliminar_view,name='medidor-delete'),

    # path('CalibracionesHistory/',views.calibracion_history_view,name='calibracion-history-list'),
    # path('MedidoresHistory/',views.medidor_history_view,name='medidor-history-list'),
]