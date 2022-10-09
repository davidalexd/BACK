from django.db import models
from django.utils import timezone
from Customer.models import AreasModel,OrganizacionModel,DepartamentoModel
from Machine.models import TuboModel,SistemaModel
from Protocol.models import ProtocolsModel,SeccionesModel,VariablesModel,PruebaCalculoModel, PruebaOpcionesModel
from CompanyMachine.models import MedidoresModel
from django.conf import settings
User = settings.AUTH_USER_MODEL


class ReportsFormatsModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="rep_frt_id")
    codigo_formato = models.CharField("Format code", max_length=255,null=True,blank=True,unique=True,db_column="rep_frt_codigo")
    nombre_formato = models.CharField("Format name", max_length=255,null=False,blank=True,db_column="rep_frt_nombre")
    
    protocolo = models.ManyToManyField(ProtocolsModel,through="Rpt_Prt_Model",through_fields=('formato', 'protocolo'))
    # variables = models.ManyToManyField(VariablesModel,through="Rpt_Var_Model",through_fields=('formato', 'variables'))
    secciones = models.ManyToManyField(SeccionesModel,through="Rpt_Secc_Model",through_fields=('formato', 'seccion'))
    calculo = models.ManyToManyField(PruebaCalculoModel,through="Rpt_Prb_Model",through_fields=('formato', 'calculo'))
    opcion = models.ManyToManyField(PruebaOpcionesModel,through="Rpt_Prb_Model",through_fields=('formato', 'opcion'))

    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsFormatsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Formatos'
    
    def __str__(self):
        return str(self.codigo_formato) + '-' + str(self.nombre_formato)

class ReportsReporteModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="rpt_id")
    fecha_control_calidad = models.DateField("QC date",auto_now_add=False,null=False,blank=False,db_column="rpt_fecha_control_calidad")
    numero_de_ot = models.CharField("Ot number",max_length=255,null=False,blank=False,db_column="rpt_numero_orden_trabajo")

    area = models.ManyToManyField(AreasModel,through="Rpt_Ar_Model",through_fields=('reportes', 'areas'))
    departamentos = models.ManyToManyField(DepartamentoModel,through="Rpt_dpt_Model",through_fields=('reportes', 'departamentos'))
    organizacion = models.ManyToManyField(OrganizacionModel,through="Rpt_org_Model",through_fields=('reportes', 'organizaciones'))

    
    valores_operaciones = models.JSONField("Values for operations",null=False,blank=False,db_column="rpt_valores_operaciones")
    
    
    sistema = models.ManyToManyField(SistemaModel,through="Rpt_Stm_Model",through_fields=('reportes', 'sistema'))
    tubo = models.ManyToManyField(TuboModel,through="Rpt_Tb_Model",through_fields=('reportes', 'tubo'))
    

    machine = models.ManyToManyField(MedidoresModel,through="Rpt_Med_Model",through_fields=('reportes', 'medidor'))

    formato = models.ManyToManyField(ReportsFormatsModel,through="Rpt_Frt_Model",through_fields=('reporte', 'formato'))


    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)


    @property
    def report_code(self):
        return 'Informe Nº '+str(self.id)+'-CCRX / OT Nº'+str(self.numero_de_ot)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(ReportsReporteModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_Reportes'

class ReportsCategoryModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="rep_cat_id")
    nombre_categoria = models.CharField("Category name", max_length=255,null=False,blank=False,db_column="rep_cat_area")
    abreviatura_categoria = models.CharField("Category abbreviation", max_length=255,null=False,blank=False,unique=True,db_column="rep_cat_abreviatura")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
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


class Frt_Cat_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="FrtCat_id")
    categoria = models.ForeignKey(ReportsCategoryModel,on_delete=models.CASCADE)
    formatos = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_formatos_categoria'



class Rpt_Ar_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    areas = models.ForeignKey(AreasModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_ar'

class Rpt_dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    departamentos = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_dpt'

class Rpt_org_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    organizaciones = models.ForeignKey(OrganizacionModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_org'


class Rpt_Frt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reporte = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Frt'

class Rpt_Tb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptTb_id")
    tubo_context_json = models.JSONField("Tube's context",null=False,blank=False,db_column="RptTb_context")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    tubo = models.ForeignKey(TuboModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Tb'

class Rpt_Stm_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptStm_id")
    sistema_context_json = models.JSONField("System's context",null=False,blank=False,db_column="RptStm_context")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    sistema = models.ForeignKey(SistemaModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Stm'
    

class Rpt_Prt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptPrt_id")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Prt'   

class Rpt_Med_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptMed_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    medidor = models.ForeignKey(MedidoresModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Med'   

class Rpt_Prb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptPrb_id")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True,blank=True)
    opcion = models.ForeignKey(PruebaOpcionesModel,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_prb'   

class Rpt_Secc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptSecc_id")
    formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,editable=False,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_secc'   

# class Rpt_Var_Model(models.Model):
#     id = models.BigAutoField(primary_key=True,db_column="RptVar_id")
#     formato = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
#     variables = models.ForeignKey(VariablesModel,on_delete=models.CASCADE)
#     created_at = models.DateTimeField(editable=False,null=False,blank=False)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.created_at = timezone.now()        
#         return super(Rpt_Var_Model, self).save(*args, **kwargs)

#     class Meta:
#         ordering = ["id"]
#         db_table = 'reports_rpt_var'   
        




class User_Reportes_Categoria_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(ReportsCategoryModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Reportes_Categoria_Model, self).save(*args, **kwargs)


class User_Reportes_Formatos_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Reportes_Formatos_Model, self).save(*args, **kwargs)


class User_Reportes_Reportes_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Reportes_Reportes_Model, self).save(*args, **kwargs)
