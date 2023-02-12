from email.policy import default
from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone

from Operations.models import VariablesModel
from Customer.models import AreasModel,OrganizacionModel,DepartamentoModel
from Machine.models import TuboModel,SistemaModel
from Protocol.models import ProtocolsModel,SeccionesModel,PruebaCalculoModel, PruebaOpcionesModel
from CompanyMachine.models import MedidoresModel

class ReportsFormatsModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="rep_frt_id")
    codigo_formato = models.CharField("Format code", max_length=255,null=True,blank=True,unique=True,db_column="rep_frt_codigo")
    nombre_formato = models.CharField("Format name", max_length=255,null=False,blank=True,db_column="rep_frt_nombre")


    protocolo = models.ManyToManyField(ProtocolsModel,through="Rpt_Prt_Model",through_fields=('formato', 'protocolo'))

    secciones = models.ManyToManyField(SeccionesModel,through="Rpt_Secc_Model",through_fields=('formato', 'seccion'))

    variables_formato = models.ManyToManyField(VariablesModel, through="Rpt_Varr_Model",through_fields=('formato', 'variable'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsFormatsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Formatos'
    
    def __str__(self):
        return str(self.codigo_formato) + '-' + str(self.nombre_formato)



class ReportsCertificadoModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="rpi_id")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsCertificadoModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Certificado'
    
    def __str__(self):
        return ' CERTIFICADO -' + str(self.id)


class ReportsReporteModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="rpt_id")
    nombre_reporte = models.CharField("Report name",max_length=255,null=True,blank=True,db_column="rpt_name_reporte")

    numero_de_ot = models.CharField("Ot number",max_length=255,null=True,blank=True,db_column="rpt_numero_orden_trabajo")
    
    fecha_control_calidad = models.DateField("QC date",null=False,blank=False,db_column="rpt_fecha_control_calidad")
    
    observacion = models.TextField("Report observacion",null=True,blank=True,db_column="rpt_observacion_reporte")

    datos_del_cliente = models.JSONField("Data for clients",null=True,blank=True,db_column="rpt_data_clientes")

    sistema = models.JSONField("Data for system",null=True,blank=True,db_column="rpt_data_sistema")
 
    componente = models.JSONField("Data for component",null=True,blank=True,db_column="rpt_data_component")
    
    machine = models.JSONField("Values for machine",null=True,blank=True,db_column="rpt_data_maquina")
    
    valores_operaciones = models.JSONField("Values for operations",null=True,blank=True,db_column="rpt_valores_operaciones")
    
    pruebas = models.JSONField("Values for Pruebas",null=True,blank=True,db_column="rpt_pruebas")

    formato = models.ManyToManyField(ReportsFormatsModel,through="Rpt_Frt_Model",through_fields=('reporte', 'formato'))

    title_image_1 = models.CharField("Title image 1", max_length=255,null=True,db_column="rpt_title_image_1")
    image_1 = models.ImageField(upload_to="reports/",blank='',default='')
    title_image_2 = models.CharField("Title image 2", max_length=255,null=True,db_column="rpt_title_image_2")
    image_2 = models.ImageField(upload_to="reports/",blank='',default='')
    title_image_3 = models.CharField("Title image 3", max_length=255,null=True,db_column="rpt_title_image_3")
    image_3 = models.ImageField(upload_to="reports/",blank='',default='',null=True)
    
    certificado = models.OneToOneField(ReportsCertificadoModel,null=True,on_delete=models.CASCADE,unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsReporteModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Reportes'








class ReportsCategoryModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="rep_cat_id")
    nombre_categoria = models.CharField("Category name", max_length=255,null=False,blank=False,db_column="rep_cat_area")
    abreviatura_categoria = models.CharField("Category abbreviation", max_length=255,null=False,blank=False,unique=True,db_column="rep_cat_abreviatura")
    members = models.ManyToManyField(ReportsFormatsModel,through="Frt_Cat_Model",through_fields=('categoria', 'formatos'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsCategoryModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Categorias'
    
    def __str__(self):
        return str(self.nombre_categoria) + '-' + str(self.abreviatura_categoria)



class Rpt_Varr_Model(models.Model):
    id= models.BigAutoField(primary_key=True,db_column="RptVar_id")
    subtitle_posicion = models.TextField("Title Seccion", null=True,blank=True,db_column="rpt_varr_seccion_title")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE, null=True,blank=True,)
    variable = models.ForeignKey(VariablesModel,on_delete=models.CASCADE, null=True,blank=True,)
    posicion = models.IntegerField("Contenedor de Variable en reporte", null=False,blank=False,db_column="rpt_varr_posicion")
    sub_posicion = models.IntegerField("Posicion de variable en contenedor",null=False,blank=False,db_column="rpt_varr_sub_posicion")
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_formatos_variables'
    


class Frt_Cat_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="FrtCat_id")
    categoria = models.ForeignKey(ReportsCategoryModel,on_delete=models.CASCADE)
    formatos = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_formatos_categoria'
    
class Rpt_Prt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptPrt_id")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    protocolo_detalles = models.JSONField("Protocol details",editable=True,null=True,blank=False,db_column="RptPrt_detalles")
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Prt'   

class Rpt_Secc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptSecc_id")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_secc'   
        
class Rpt_Frt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reporte = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Frt'
