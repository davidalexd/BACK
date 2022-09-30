from django.contrib import admin
from .models import ReportsFormatsModel,ReportsCategoryModel,ReportsReporteModel,Frt_Cat_Model,Rpt_Ar_Model,Rpt_Frt_Model, Rpt_Stm_Model,Rpt_Tb_Model,Rpt_Prt_Model,Rpt_Prb_Model,Rpt_Med_Model, Rpt_Var_Model, Rpt_dpt_Model, Rpt_org_Model

class FormatoCategoria(admin.TabularInline):
    model = Frt_Cat_Model
    extra = 1

class ReportesArea(admin.TabularInline):
    model = Rpt_Ar_Model
    extra = 1

class ReportesDepartamento(admin.TabularInline):
    model = Rpt_dpt_Model
    extra = 1

class ReportesOrganizacion(admin.TabularInline):
    model = Rpt_org_Model
    extra = 1

class ReportesFormatos(admin.TabularInline):
    model = Rpt_Frt_Model
    extra = 1

class ReportesTubo(admin.TabularInline):
    model = Rpt_Tb_Model
    extra = 1

class ReportesSistema(admin.TabularInline):
    model = Rpt_Stm_Model
    extra = 1

class ReportesProtocolos(admin.TabularInline):
    model = Rpt_Prt_Model
    extra = 1

class ReportesPruebas(admin.TabularInline):
    model = Rpt_Prb_Model
    extra = 1  

class ReportesVariables(admin.TabularInline):
    model = Rpt_Var_Model
    extra = 1  

class MedidorProtocolos(admin.TabularInline):
    model = Rpt_Med_Model
    extra = 1

@admin.register(ReportsCategoryModel)
class ReportsCategoryModel(admin.ModelAdmin):
    inlines = [FormatoCategoria,]
    list_display = ("id","nombre_categoria","abreviatura_categoria","is_enabled","created_at")
    search_fields = ('nombre_categoria',)
    list_filter = ('abreviatura_categoria','members')
    filter_horizontal = ['members']


@admin.register(ReportsFormatsModel)
class ReportsFormatsModel(admin.ModelAdmin):
    list_display = ("id","codigo_formato","nombre_formato","is_enabled","created_at")


@admin.register(ReportsReporteModel)
class ReportsReportesModel(admin.ModelAdmin):
    inlines = [ReportesArea,ReportesDepartamento,ReportesOrganizacion,ReportesFormatos,ReportesTubo,ReportesSistema,ReportesProtocolos,MedidorProtocolos,ReportesPruebas,ReportesVariables]
    list_display = ("report_code","fecha_control_calidad","is_enabled","created_at",)
    search_fields = ('id',)
    list_filter = ('id','area','departamentos','organizacion','tubo','protocolo','machine')
    filter_horizontal = ['organizacion','tubo','protocolo','machine']


