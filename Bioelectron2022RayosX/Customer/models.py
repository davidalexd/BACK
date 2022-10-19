from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone

class ContactosModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="con_id")
    nombre = models.CharField("Contact's name",default="---",max_length=255,null=True,blank=True,unique=False,db_column="con_nombre")
    apellidos = models.CharField("Contact's last name",default="---",max_length=255,null=True,blank=True,unique=False,db_column="con_apellidos")
    dni = models.CharField("Contact's DNI number",default="---",max_length=255,null=True,blank=True,unique=False,db_column="con_numero_dni")
    numero_telefono = models.CharField("Contact phone number",default="---", max_length=255,null=True,blank=True,db_column="con_numero_telefono")    
    correo = models.CharField("Contact email address",default="---", max_length=255,null=True,blank=True,db_column="con_correo_electronico")    
    cargo = models.CharField("Job",default="---", max_length=255,null=True,blank=True,db_column="con_cargo")    
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ContactosModel, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.nombre+' '+ self.apellidos

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Contactos'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidos

class AreasModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="ar_id")
    nombre_area = models.CharField("Area's name",editable=True,max_length=255,null=False,blank=False,unique=False,db_column="ar_nombre_area")
    ubicacion = models.JSONField("Area's location",editable=True,null=True,blank=False,db_column="ar_ubicacion_area")    

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(AreasModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Ambientes'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_area

class DepartamentoModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="dpt_id")
    nombre_departamento = models.CharField("Headquarters's name",max_length=255,null=False,blank=False,unique=False,db_column="dpt_nombre_departamento")
    direccion_departamento = models.CharField("Headquarters's address", max_length=255,null=True,blank=True,db_column="dpt_direccion_departamento")
    pais_departamento = models.CharField("Country where the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_pais")
    departamento_departamento = models.CharField("Department to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_departamento")
    provincia_departamento = models.CharField("Province to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_provincia")
    distrito_departamento = models.CharField("District to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_distrito")
    members = models.ManyToManyField(AreasModel,through="Ar_dpt_Model",through_fields=('departamento', 'area'))
    contactos = models.ManyToManyField(ContactosModel,through="Con_Dpt_Model",through_fields=('departamento', 'contacto'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(DepartamentoModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Depatamentos'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_departamento

class OrganizacionModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="org_id")
    ruc = models.CharField("Organization's ruc number",max_length=12,null=True,blank=True,unique=True,db_column="org_ruc")
    razon_social = models.CharField("Organization's name",max_length=255,null=False,blank=True,unique=True,db_column="org_razon_social")
    nombre_comercial = models.CharField("Organization's commercial name ",max_length=255,null=True,blank=True,unique=True,db_column="org_nombre_comercial")
    tipo = models.CharField("Organization's type", max_length=255,null=True,blank=True,db_column="org_tipo")
    ciiu = models.IntegerField("Organization's International Standard Industrial Classification",null=True,blank=True,db_column="org_ciiu")
    direccion_legal = models.CharField("Organization's legal address", max_length=255,null=True,blank=True,db_column="org_direccion_legal")
    pais_organizacion = models.CharField("Country where the organization belongs", max_length=255,null=True,blank=True,db_column="org_pais")
    departamento_organizacion = models.CharField("Department to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_departamento")
    provincia_organizacion = models.CharField("Province to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_provincia")
    distrito_organizacion = models.CharField("District to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_distrito")
    members = models.ManyToManyField(DepartamentoModel,through="Dpt_org_Model",through_fields=('organizacion', 'departamento'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(OrganizacionModel, self).save(*args, **kwargs)

    @property
    def full_direction(self):
        return str(self.direccion_legal) +' '+ str(self.pais_organizacion) +' - '+ str(self.departamento_organizacion) +' - '+ str(self.provincia_organizacion) +' - '+ str(self.distrito_organizacion)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Organizaciones'

    def __str__(self):
        return str(self.id) + '-' + self.razon_social


class Dpt_org_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="DptOrg_id")
    organizacion = models.ForeignKey(OrganizacionModel,on_delete=models.CASCADE)
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=True,blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_organizacion_departamentos'

class Ar_dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="ArDpt_id")
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    area = models.ForeignKey(AreasModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_departamento_ambiente'

class Con_Dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="ConDpt_id")
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    contacto = models.ForeignKey(ContactosModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_contactos_departamento'

