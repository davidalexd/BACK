from django.urls import path
from . import views

urlpatterns = [
    path('Formats/',views.formatos_create_view,name='formatos-list'),
    path('CategoryFormats/',views.categorias_create_view,name='categorias-formatos-list')
]