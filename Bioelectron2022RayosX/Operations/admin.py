from django.contrib import admin
from .models import Cat_Category_Operaciones, CategoryOperacionesModel, OperacionesModel,Opr_Operacion_Variables, VariablesModel

class OperacionVariables(admin.TabularInline):
    model = Opr_Operacion_Variables
    extra = 1

class CategoriaOperaciones(admin.TabularInline):
    model = Cat_Category_Operaciones
    extra = 1

@admin.register(CategoryOperacionesModel)
class CategoryOperacionesAdmin(admin.ModelAdmin):
    inlines = [CategoriaOperaciones]
    list_display = ("id","category_operacion_titulo","category_operacion_contexto","is_enabled","created_at")
    search_fields = ('category_operacion_titulo',)
    list_filter = ('category_operacion_titulo',)

@admin.register(OperacionesModel)
class OperacionesAdmin(admin.ModelAdmin):
    inlines = [OperacionVariables]
    list_display = ("id","operacion_titulo","operacion_symbol","operacion_variable","operacion_contexto","is_enabled","created_at")
    search_fields = ('operacion_titulo',)
    list_filter = ('operacion_titulo',)
    
@admin.register(VariablesModel)
class VariablesAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_variable","range_variable","is_enabled","created_at")
