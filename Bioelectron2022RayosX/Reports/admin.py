from django.contrib import admin
from .models import ReportsFormatsModel,ReportsCategoryModel,Frt_Cat_Model

class FormatoCategoria(admin.TabularInline):
    model = Frt_Cat_Model
    extra = 1

@admin.register(ReportsCategoryModel)
class ReportsCategoryModel(admin.ModelAdmin):
    inlines = [FormatoCategoria,]
    list_display = ("id","nombre_categoria","abreviatura_categoria","is_enabled","crated_at")
    search_fields = ('nombre_categoria',)
    list_filter = ('abreviatura_categoria','members')
    filter_horizontal = ['members']


@admin.register(ReportsFormatsModel)
class ReportsFormatsModel(admin.ModelAdmin):
    list_display = ("id","codigo_formato","nombre_formato","is_enabled","crated_at")


