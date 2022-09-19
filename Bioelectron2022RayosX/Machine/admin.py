from django.contrib import admin
from .models import SistemaModel,TuboModel

@admin.register(SistemaModel)
class SistemaModel(admin.ModelAdmin):
    list_display = ('id',"marca","modelo","serie","antiguedad_year","year_instalacion","is_enabled","crated_at")

@admin.register(TuboModel)
class TuboModel(admin.ModelAdmin):
    list_display = ('id',"marca","modelo","serie","antiguedad_year","year_instalacion","is_enabled","crated_at")