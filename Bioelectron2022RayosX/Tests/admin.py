from django.contrib import admin
from .models import PruebasModel,PruebaCalculo,PruebaOpciones,PruebaCalculoRelacion,Prb_Cal_Opr_Model,Prb_Calculo_Model,Prb_PrbRelacion_Model

class PruebaCalculoOperaciones(admin.TabularInline):
    model = Prb_Cal_Opr_Model
    extra = 1

class PruebaCalculoTipo(admin.TabularInline):
    model = Prb_Calculo_Model
    extra = 1

class PruebaCalculoRelacionTipo(admin.TabularInline):
    model = Prb_PrbRelacion_Model
    extra = 1


@admin.register(PruebaCalculo)
class PruebaCalculo(admin.ModelAdmin):
    inlines = [PruebaCalculoOperaciones,PruebaCalculoRelacionTipo]
    list_display = ("id","variable","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","crated_at")

@admin.register(PruebaCalculoRelacion)
class PruebaCalculoRelacion(admin.ModelAdmin):
    inlines = [PruebaCalculoOperaciones,]
    list_display = ("id","variable","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","crated_at")


@admin.register(PruebaOpciones)
class PruebaOpciones(admin.ModelAdmin):
    list_display = ("id","pruebas_opciones","is_enabled","crated_at")


@admin.register(PruebasModel)
class PruebasModel(admin.ModelAdmin):
    inlines = [PruebaCalculoTipo,]
    list_display = ("id","pruebas_titulo","pruebas_contexto","is_enabled","crated_at")
    search_fields = ('pruebas_titulo','calculo','calculo_relacion','opcion',)
    list_filter = ('pruebas_titulo','calculo','calculo_relacion','opcion',)
