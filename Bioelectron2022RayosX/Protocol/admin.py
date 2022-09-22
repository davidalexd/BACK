from django.contrib import admin
from .models import ProtocolsModel,SeccionesModel,PruebasModel,Prt_Scc_Model,Scc_Prb_Model


class ProtocoloSeccion(admin.TabularInline):
    model = Prt_Scc_Model
    extra = 1

class SeccionPrueba(admin.TabularInline):
    model = Scc_Prb_Model
    extra = 1


@admin.register(SeccionesModel)
class SeccionesModel(admin.ModelAdmin):
    inlines = [SeccionPrueba,]
    list_display = ("id","secciones_titulo","secciones_contexto","is_enabled","crated_at")
    search_fields = ('secciones_titulo',)
    list_filter = ('secciones_titulo',)
    
@admin.register(ProtocolsModel)
class ProtocolsModel(admin.ModelAdmin):
    inlines = [ProtocoloSeccion,]
    list_display = ("id","protocolo_titulo","protocolo_detalles","is_enabled","crated_at")
    search_fields = ('protocolo_titulo',)
    list_filter = ('protocolo_titulo',)
    