from django.contrib import admin
from .models import OrganizacionModel,DepartamentoModel,AreasModel,ContactosModel,Dpt_org_Model,Ar_dpt_Model,Con_Dpt_Model,User_Organizaciones_Model

class DepartemantosOrganizacion(admin.TabularInline):
    model = Dpt_org_Model
    extra = 1

class AreasDepartamento(admin.TabularInline):
    model = Ar_dpt_Model
    extra = 1

class ContactosDepartamento(admin.TabularInline):
    model = Con_Dpt_Model
    extra = 1


class UserOrganizaciones(admin.TabularInline):
    model = User_Organizaciones_Model
    extra = 1


@admin.register(OrganizacionModel)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [DepartemantosOrganizacion,UserOrganizaciones]
    list_display = ("id","razon_social","ruc","nombre_comercial","tipo","ciiu","direccion_legal","pais_organizacion","departamento_organizacion","provincia_organizacion","distrito_organizacion","is_enabled","created_at")


@admin.register(DepartamentoModel)
class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [AreasDepartamento,ContactosDepartamento,]
    list_display = ("id","nombre_departamento","direccion_departamento","pais_departamento","departamento_departamento","provincia_departamento","distrito_departamento","is_enabled","created_at")

@admin.register(AreasModel)
class AreasAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_area","ubicacion","is_enabled","created_at")


@admin.register(ContactosModel)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","nombre","apellidos","dni","numero_telefono","correo","is_enabled","created_at")