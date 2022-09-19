from django.contrib import admin
from .models import OrganizacionModel,DepartamentoModel,AreasModel,ContactosModel,Dpt_org_Model,Ar_dpt_Model,Con_Dpt_Model

class DepartemantosOrganizacion(admin.TabularInline):
    model = Dpt_org_Model
    extra = 1

class AreasDepartamento(admin.TabularInline):
    model = Ar_dpt_Model
    extra = 1

class ContactosDepartamento(admin.TabularInline):
    model = Con_Dpt_Model
    extra = 1

@admin.register(OrganizacionModel)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [DepartemantosOrganizacion,]
    list_display = ("id","razon_social","ruc","nombre_comercial","tipo","ciiu","direccion_legal","pais","departamento","provincia","distrito","is_enabled","crated_at")
    search_fields = ('razon_social',)
    list_filter = ('ruc','members',)
    filter_horizontal = ['members',]


@admin.register(DepartamentoModel)
class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [AreasDepartamento,ContactosDepartamento,]
    list_display = ("id","nombre_departamento","direccion_departamento","pais","departamento","provincia","distrito","is_enabled","crated_at")
    search_fields = ('nombre_departamento',)
    list_filter = ('nombre_departamento','members','contactos',)
    filter_horizontal = ['members','contactos',]

@admin.register(AreasModel)
class AreasAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_area","ubicacion","is_enabled","crated_at")


@admin.register(ContactosModel)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","dni","numero_telefono","correo","is_enabled","crated_at")