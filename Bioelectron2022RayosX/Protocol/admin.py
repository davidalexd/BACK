from django.contrib import admin
from .models import ProtocolsModel

@admin.register(ProtocolsModel)
class ProtocolModel(admin.ModelAdmin):
    list_display = ("id","nombre_protocolo","detalles_protocolo","is_enabled","crated_at")
    search_fields = ('nombre_protocolo',)
    list_filter = ('nombre_protocolo',)
    
