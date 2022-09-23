from django.contrib import admin
from .models import ReportsFormatsModel,ReportsCategoryModel,ReportsReporteModel,Frt_Cat_Model,Rpt_Ar_Model,Rpt_Frt_Model,Rpt_Tb_Model,Rpt_Prt_Model,Rpt_Prb_Model,Rpt_Med_Model

class FormatoCategoria(admin.TabularInline):
    model = Frt_Cat_Model
    extra = 1

class ReportesArea(admin.TabularInline):
    model = Rpt_Ar_Model
    extra = 1

class ReportesFormatos(admin.TabularInline):
    model = Rpt_Frt_Model
    extra = 1

class ReportesTubo(admin.TabularInline):
    model = Rpt_Tb_Model
    extra = 1

class ReportesProtocolos(admin.TabularInline):
    model = Rpt_Prt_Model
    extra = 1

class ReportesPruebas(admin.TabularInline):
    model = Rpt_Prb_Model
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
    inlines = [ReportesArea,ReportesFormatos,ReportesTubo,ReportesProtocolos,MedidorProtocolos,ReportesPruebas]
    list_display = ("report_code","fecha_control_calidad","is_enabled","created_at",)
    search_fields = ('id',)
    list_filter = ('id','cliente','tubo','protocolo','machine')
    filter_horizontal = ['cliente','tubo','protocolo','machine']


