from django.db import models
from django.utils import timezone
from Customer.models import AreasModel,OrganizacionModel,DepartamentoModel
from Machine.models import TuboModel,SistemaModel
from Protocol.models import ProtocolsModel,SeccionesModel,VariablesModel,PruebaCalculoModel, PruebaOpcionesModel
from CompanyMachine.models import MedidoresModel


class ReportsFormatsModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="rep_frt_id")
    codigo_formato = models.CharField("Format code", max_length=255,null=True,blank=True,unique=True,db_column="rep_frt_codigo")
    nombre_formato = models.CharField("Format name", max_length=255,null=False,blank=True,db_column="rep_frt_nombre")
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
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Frt_Cat_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_formatos_categoria'

class ReportsReporteModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="rpt_id")
    fecha_control_calidad = models.DateField("QC date",auto_now_add=False,null=False,blank=False,db_column="rpt_fecha_control_calidad")
    numero_de_ot = models.CharField("Ot number",max_length=255,null=False,blank=False,db_column="rpt_numero_orden_trabajo")

    area = models.ManyToManyField(AreasModel,through="Rpt_Ar_Model",through_fields=('reportes', 'areas'))
    departamentos = models.ManyToManyField(DepartamentoModel,through="Rpt_dpt_Model",through_fields=('reportes', 'departamentos'))
    organizacion = models.ManyToManyField(OrganizacionModel,through="Rpt_org_Model",through_fields=('reportes', 'organizaciones'))

    formato = models.ManyToManyField(ReportsFormatsModel,through="Rpt_Frt_Model",through_fields=('reportes', 'formatos'))
    
    
    sistema = models.ManyToManyField(SistemaModel,through="Rpt_Stm_Model",through_fields=('reportes', 'sistema'))
    tubo = models.ManyToManyField(TuboModel,through="Rpt_Tb_Model",through_fields=('reportes', 'tubo'))
    

    machine = models.ManyToManyField(MedidoresModel,through="Rpt_Med_Model",through_fields=('reportes', 'medidor'))


    protocolo = models.ManyToManyField(ProtocolsModel,through="Rpt_Prt_Model",through_fields=('reportes', 'protocolo'))
    variables = models.ManyToManyField(VariablesModel,through="Rpt_Var_Model",through_fields=('reportes', 'variables'))
    secciones = models.ManyToManyField(SeccionesModel,through="Rpt_Secc_Model",through_fields=('reportes', 'seccion'))
    calculo = models.ManyToManyField(PruebaCalculoModel,through="Rpt_Prb_Model",through_fields=('reportes', 'calculo'))
    opcion = models.ManyToManyField(PruebaOpcionesModel,through="Rpt_Prb_Model",through_fields=('reportes', 'opcion'))


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


class Rpt_Ar_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    areas = models.ForeignKey(AreasModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Ar_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_ar'

class Rpt_dpt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    departamentos = models.ForeignKey(DepartamentoModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_dpt_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_dpt'

class Rpt_org_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    organizaciones = models.ForeignKey(OrganizacionModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_org_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_org'


class Rpt_Frt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptAr_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    formatos = models.ForeignKey(ReportsFormatsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Frt_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Frt'

class Rpt_Tb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptTb_id")
    tubo_context_json = models.JSONField("Tube's context",null=False,blank=False,db_column="RptTb_context")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    tubo = models.ForeignKey(TuboModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Tb_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Tb'

class Rpt_Stm_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptStm_id")
    sistema_context_json = models.JSONField("System's context",null=False,blank=False,db_column="RptStm_context")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    sistema = models.ForeignKey(SistemaModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Stm_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Stm'
    

class Rpt_Prt_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptPrt_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Prt_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Prt'   

class Rpt_Med_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptMed_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    medidor = models.ForeignKey(MedidoresModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Med_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_Med'   

class Rpt_Prb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptPrb_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE)
    opcion = models.ForeignKey(PruebaOpcionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Prb_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_prb'   

class Rpt_Secc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptSecc_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Secc_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_secc'   

class Rpt_Var_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="RptVar_id")
    reportes = models.ForeignKey(ReportsReporteModel,on_delete=models.CASCADE)
    variables = models.ForeignKey(VariablesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Rpt_Var_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_rpt_var'   
        