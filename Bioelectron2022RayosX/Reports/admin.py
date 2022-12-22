from django.contrib import admin
from .models import ReportsFormatsModel,ReportsCategoryModel,ReportsReporteModel,Frt_Cat_Model,Rpt_Frt_Model, Rpt_Secc_Model,Rpt_Prt_Model, Rpt_Varr_Model,ReportsCertificadoModel

class FormatoCategoria(admin.TabularInline):
    model = Frt_Cat_Model
    extra = 1


class ReportesFormatos(admin.TabularInline):
    model = Rpt_Frt_Model
    extra = 1

class ReportesProtocolos(admin.TabularInline):
    model = Rpt_Prt_Model
    extra = 1

class ReportesSecciones(admin.TabularInline):
    model = Rpt_Secc_Model
    extra = 1

class FormatoVariables(admin.TabularInline):
    model = Rpt_Varr_Model
    extra = 1

@admin.register(ReportsCategoryModel)
class ReportsCategoryModel(admin.ModelAdmin):
    inlines = [FormatoCategoria]
    list_display = ("id","nombre_categoria","abreviatura_categoria","is_enabled","created_at")
    search_fields = ('nombre_categoria',)
    list_filter = ('abreviatura_categoria','members')
    filter_horizontal = ['members']


@admin.register(ReportsFormatsModel)
class ReportsFormatsModel(admin.ModelAdmin):
    inlines = [ReportesProtocolos,ReportesSecciones,FormatoVariables]
    list_display = ("id","codigo_formato","nombre_formato","is_enabled","created_at")


@admin.register(ReportsReporteModel)
class ReportsReportesModel(admin.ModelAdmin):
    inlines = [ReportesFormatos]
    list_display = (
        "id",
        "numero_de_ot",
        "certificado",
        "fecha_control_calidad",
        "pruebas",
        "datos_del_cliente",
        "sistema",
        "componente",
        "machine",
        "image_1",
        "image_2",
        "image_3",
        "valores_operaciones",
        "created_at",
        "is_enabled",
    )
    search_fields = ('id',)
    list_filter = ('id','formato',)
    filter_horizontal = ['formato']


@admin.register(ReportsCertificadoModel)
class ReportsInformesModel(admin.ModelAdmin):
    list_display = ("id","is_enabled","created_at")

