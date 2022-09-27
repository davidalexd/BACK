from django.contrib import admin
from .models import MedidoresModel,CalibracionesModel,Cal_Med_Model

class CalibracionMedicion(admin.TabularInline):
    model = Cal_Med_Model
    extra = 1

@admin.register(MedidoresModel)
class MedidoresModel(admin.ModelAdmin):
    inlines = [CalibracionMedicion,]
    list_display = ("id","marca","modelo","serie","is_enabled","created_at")
    search_fields = ('marca',)
    list_filter = ('marca','members')
    filter_horizontal = ['members']


@admin.register(CalibracionesModel)
class CalibracionesModel(admin.ModelAdmin):
    list_display = ("id","fecha_calibracion","is_enabled","created_at")




