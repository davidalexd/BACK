from django.contrib import admin
from Protocol.models import VariablesModel,PruebaCalculoModel,PruebaOpcionesModel,PruebasModel,ProtocolsModel, SeccionesModel,Prb_Calculo_Operacion_Model,Prueba_Tipo_Model,Prt_Scc_Model,Prt_Var_Model,Scc_Prb_Model,Prb_Operacion_Variables

class CalculoOperacion(admin.TabularInline):
    model = Prb_Calculo_Operacion_Model
    extra = 1

class TipoPrueba(admin.TabularInline):
    model = Prueba_Tipo_Model
    extra = 1

class ProtocoloSecciones(admin.TabularInline):
    model = Prt_Scc_Model
    extra = 1

class ProtocoloVariables(admin.TabularInline):
    model = Prt_Var_Model
    extra = 1

class SeccionVariables(admin.TabularInline):
    model = Scc_Prb_Model
    extra = 1

class CalculoOperacionesVariables(admin.TabularInline):
    model = Prb_Operacion_Variables
    extra = 1

@admin.register(VariablesModel)
class VariablesAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_variable","range_variable","is_enabled","created_at")

@admin.register(PruebaCalculoModel)
class PruebaCalculoAdmin(admin.ModelAdmin):
    inlines = [CalculoOperacion,]
    list_display = ("id","pruebas_resultado","pruebas_tolerancia","pruebas_condicion_respuesta","is_enabled","created_at")


@admin.register(PruebaOpcionesModel)
class PruebaOpcioneAdmin(admin.ModelAdmin):
    list_display = ("id","pruebas_opciones","is_enabled","created_at")

@admin.register(PruebasModel)
class PruebaAdmin(admin.ModelAdmin):
    inlines = [TipoPrueba,]
    list_display = ("id","pruebas_titulo","pruebas_contexto","is_enabled","created_at")

@admin.register(SeccionesModel)
class SeccionAdmin(admin.ModelAdmin):
    inlines = [SeccionVariables,]
    list_display = ("id","secciones_titulo","secciones_contexto","is_enabled","created_at")

@admin.register(ProtocolsModel)
class ProtocoloAdmin(admin.ModelAdmin):
    inlines = [ProtocoloSecciones,ProtocoloVariables]
    list_display = ("id","protocolo_titulo","protocolo_detalles","is_enabled","created_at")