from django.contrib import admin
from .models import PruebaVariableModel,PruebaCalculoRelacionModel,PruebaCalculoModel,PruebaOpcionesModel,PruebasModel,Prb_PrbRelacion_Model,Prb_Calculo_Model,Prb_Cal_Opr_Model,Prb_Cal_Opr_Val_Model

class PruebaCalculoOperacionesVariables(admin.TabularInline):
    model = Prb_Cal_Opr_Val_Model
    extra = 1

class PruebaCalculoOperaciones(admin.TabularInline):
    model = Prb_Cal_Opr_Model
    extra = 1

class PruebaCalculoTipo(admin.TabularInline):
    model = Prb_Calculo_Model
    extra = 1

class PruebaCalculoRelacionTipo(admin.TabularInline):
    model = Prb_PrbRelacion_Model
    extra = 1

@admin.register(Prb_Cal_Opr_Model)
class PruebaOperacionesVariablesAdmin(admin.ModelAdmin):
    inlines = [PruebaCalculoOperacionesVariables,]
    list_display = ("id","calculo","calculo_relacion","operacion","crated_at")

@admin.register(PruebaVariableModel)
class PruebaVariablesAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_variable","rango_variable","is_enabled","crated_at")

@admin.register(PruebaCalculoModel)
class PruebaCalculoAdmin(admin.ModelAdmin):
    inlines = [PruebaCalculoOperaciones]
    list_display = ("id","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","crated_at")

@admin.register(PruebaCalculoRelacionModel)
class PruebaCalculoRelacionAdmin(admin.ModelAdmin):
    inlines = [PruebaCalculoRelacionTipo,PruebaCalculoOperaciones]
    list_display = ("id","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","crated_at")


@admin.register(PruebaOpcionesModel)
class PruebaOpcionesAdmin(admin.ModelAdmin):
    list_display = ("id","pruebas_opciones","is_enabled","crated_at")


@admin.register(PruebasModel)
class PruebasAdmin(admin.ModelAdmin):
    inlines = [PruebaCalculoTipo,]
    list_display = ("id","pruebas_titulo","pruebas_contexto","is_enabled","crated_at")
    search_fields = ('pruebas_titulo','calculo','calculo_relacion','opcion',)
    list_filter = ('pruebas_titulo','calculo','calculo_relacion','opcion',)
