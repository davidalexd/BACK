from django.contrib import admin
from .models import OperacionesModel

@admin.register(OperacionesModel)
class OperacionesModel(admin.ModelAdmin):
    list_display = ("id","operacion_titulo","operacion_contexto","is_enabled","created_at")
    search_fields = ('operacion_titulo',)
    list_filter = ('operacion_titulo',)
    
