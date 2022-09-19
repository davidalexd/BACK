from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class ContactosModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="con_id")
    nombre = models.CharField("Contact's name",max_length=255,null=False,blank=False,unique=False,db_column="con_nombre")
    apellidos = models.CharField("Contact's last name",max_length=255,null=False,blank=False,unique=False,db_column="con_apellidos")
    dni = models.CharField("Contact's DNI number",max_length=255,null=True,blank=True,unique=True,db_column="con_numero_dni")
    numero_telefono = models.CharField("Contact phone number", max_length=255,null=True,blank=True,db_column="con_numero_telefono")    
    correo = models.CharField("Contact email address", max_length=255,null=True,blank=True,unique=True,db_column="con_correo_electronico")    
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(ContactosModel, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.nombre+' '+ self.apellidos

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Contactos'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellidos

class AreasModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="ar_id")
    nombre_area = models.CharField("Area's name",max_length=255,null=False,blank=False,unique=False,db_column="ar_nombre_area")
    ubicacion = models.CharField("Area location", max_length=255,null=False,blank=False,db_column="ar_ubicacion_area")    
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(AreasModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Ambientes'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_area + '-' + self.ubicacion

class DepartamentoModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="dpt_id")
    nombre_departamento = models.CharField("Headquarters's name",max_length=255,null=False,blank=False,unique=False,db_column="dpt_nombre_departamento")
    direccion_departamento = models.CharField("Headquarters's address", max_length=255,null=True,blank=True,db_column="dpt_direccion_departamento")
    pais = models.CharField("Country where the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_pais")
    departamento = models.CharField("Department to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_departamento")
    provincia = models.CharField("Province to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_provincia")
    distrito = models.CharField("District to which the headquarters belongs", max_length=255,null=True,blank=True,db_column="dpt_distrito")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    members = models.ManyToManyField(AreasModel,through="Ar_dpt_Model",through_fields=('departamento', 'area'))
    contactos = models.ManyToManyField(ContactosModel,through="Con_Dpt_Model",through_fields=('departamento', 'contacto'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(DepartamentoModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Depatamentos'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_departamento

class OrganizacionModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="org_id")
    ruc = models.CharField("Organization's ruc number",max_length=12,null=True,blank=True,unique=True,db_column="org_ruc")
    razon_social = models.CharField("Organization's name",max_length=255,null=False,blank=False,unique=True,db_column="org_razon_social")
    nombre_comercial = models.CharField("Organization's commercial name ",max_length=255,null=True,blank=True,unique=True,db_column="org_nombre_comercial")
    tipo = models.CharField("Organization's type", max_length=255,null=True,blank=True,db_column="org_tipo")
    ciiu = models.IntegerField("Organization's International Standard Industrial Classification",null=True,blank=True,db_column="org_ciiu")
    direccion_legal = models.CharField("Organization's legal address", max_length=255,null=True,blank=True,db_column="org_direccion_legal")
    pais = models.CharField("Country where the organization belongs", max_length=255,null=True,blank=True,db_column="org_pais")
    departamento = models.CharField("Department to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_departamento")
    provincia = models.CharField("Province to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_provincia")
    distrito = models.CharField("District to which the organization belongs", max_length=255,null=True,blank=True,db_column="org_distrito")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    members = models.ManyToManyField(DepartamentoModel,through="Dpt_org_Model",through_fields=('organizacion', 'departamento'))


    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(OrganizacionModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_Organizaciones'

    def __str__(self):
        return str(self.id) + '-' + self.razon_social


class Dpt_org_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="DptOrg_id")
    organizacion = models.ForeignKey(OrganizacionModel,on_delete=models.CASCADE)
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Dpt_org_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_organizacion_departamentos'

class Ar_dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="ArDpt_id")
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    area = models.ForeignKey(AreasModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Ar_dpt_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_departamento_ambiente'

class Con_Dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="ConDpt_id")
    departamento = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    contacto = models.ForeignKey(ContactosModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Con_Dpt_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'customers_contactos_departamento'



