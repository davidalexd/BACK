from django.contrib import admin
from .models import SistemaModel,TuboModel,Stm_Tb_Model

class SistemaTubos(admin.TabularInline):
    model = Stm_Tb_Model
    extra = 1

@admin.register(SistemaModel)
class SistemaModel(admin.ModelAdmin):
    inlines = [SistemaTubos,]
    list_display = ('id',"marca","modelo","serie","antiguedad_year","year_instalacion","is_enabled","created_at")
    search_fields = ('marca','modelo','serie',)
    list_filter = ('marca','members')
    filter_horizontal = ['members']
    
@admin.register(TuboModel)
class TuboModel(admin.ModelAdmin):
    list_display = ('id',"marca","modelo","serie","antiguedad_year","year_instalacion","is_enabled","created_at")