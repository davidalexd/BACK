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
    inlines = [DepartemantosOrganizacion]
    list_display = ("id","razon_social","ruc","nombre_comercial","tipo","ciiu","direccion_legal","pais_organizacion","departamento_organizacion","provincia_organizacion","distrito_organizacion")


@admin.register(DepartamentoModel)
class DepartamentoAdmin(admin.ModelAdmin):
    inlines = [AreasDepartamento,ContactosDepartamento,]
    list_display = ("id","nombre_departamento","direccion_departamento","pais_departamento","departamento_departamento","provincia_departamento","distrito_departamento")

@admin.register(AreasModel)
class AreasAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_area","ubicacion")


@admin.register(ContactosModel)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ("id","full_name","nombre","apellidos","dni","numero_telefono","correo")