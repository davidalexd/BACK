from django.urls import path
from . import views

urlpatterns = [
    path('Formats/',views.formatos_create_view,name='formato-reporte-list'),
    path('Formats/<int:pk>/',views.formatos_list_view,name='formato-reporte-detail'),
    path('Formats/<int:pk>/update/',views.formatos_actualizar_view,name='formato-reporte-update'),
    path('Formats/<int:pk>/delete/',views.formatos_eliminar_view,name='formato-reporte-delete'),

    path('CategoryFormats/',views.categorias_create_view,name='categoria-reporte-list'),
    path('CategoryFormats/<int:pk>/',views.categorias_list_view,name='categoria-reporte-detail'),
    path('CategoryFormats/<int:pk>/update/',views.categorias_actualizar_view,name='categoria-reporte-update'),
    path('CategoryFormats/<int:pk>/delete/',views.categorias_eliminar_view,name='categoria-reporte-delete'),

    path('ReportFormats/',views.reportes_create_view,name='reporte-reporte-list'),
    path('ReportFormats/<int:pk>/',views.reportes_list_view,name='reporte-reporte-detail'),
    path('ReportFormats/<int:pk>/update/',views.reportes_actualizar_view,name='reporte-reporte-update'),
    path('ReportFormats/<int:pk>/delete/',views.reportes_eliminar_view,name='reporte-reporte-delete')
]