from django.contrib import admin
from Protocol.models import PruebaCalculoModel,PruebaOpcionesModel,ProtocolsModel, SeccionesModel,Prb_Calculo_Operacion_Model,Prueba_Tipo_Model,Prt_Scc_Model

class CalculoOperacion(admin.TabularInline):
    model = Prb_Calculo_Operacion_Model
    extra = 1

class TipoPrueba(admin.TabularInline):
    model = Prueba_Tipo_Model
    extra = 1


class ProtocoloSecciones(admin.TabularInline):
    model = Prt_Scc_Model
    extra = 1


@admin.register(PruebaCalculoModel)
class PruebaCalculoAdmin(admin.ModelAdmin):
    inlines = [CalculoOperacion,]
    list_display = ("id","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","created_at")


@admin.register(PruebaOpcionesModel)
class PruebaOpcioneAdmin(admin.ModelAdmin):
    list_display = ("id","pruebas_opciones","is_enabled","created_at")


@admin.register(SeccionesModel)
class SeccionAdmin(admin.ModelAdmin):
    inlines = [TipoPrueba,]
    list_display = ("id","secciones_titulo","secciones_contexto","is_enabled","created_at")

@admin.register(ProtocolsModel)
class ProtocoloAdmin(admin.ModelAdmin):
    inlines = [ProtocoloSecciones]
    list_display = ("id","protocolo_titulo","is_enabled","created_at")
