from django.contrib import admin
from .models import InspeccionesFisicasModel

@admin.register(InspeccionesFisicasModel)
class InspeccionesFisicasModel(admin.ModelAdmin):
    list_display = ("id","inspeccion_fisica_titulo","is_enabled","crated_at")
    search_fields = ('inspeccion_fisica_titulo',)
    list_filter = ('inspeccion_fisica_titulo',)
    
