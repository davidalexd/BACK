from django.contrib import admin
from .models import SistemaModel,TuboModel,Stm_Tb_Model

class SistemaTubos(admin.TabularInline):
    model = Stm_Tb_Model
    extra = 1

@admin.register(SistemaModel)
class SistemaModel(admin.ModelAdmin):
    inlines = [SistemaTubos,]
    list_display = ('id','title',"marca","name_option","modelo","antiguedad_year","year_instalacion","is_enabled","created_at")
    search_fields = ('marca','modelo',)
    list_filter = ('marca','members')
    filter_horizontal = ['members']
    
@admin.register(TuboModel)
class TuboModel(admin.ModelAdmin):
    list_display = ('id','title','name_option',"marca","modelo","antiguedad_year","year_instalacion","is_enabled","created_at")