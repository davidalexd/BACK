from django.db import models
from django.utils import timezone
from Operations.models import OperacionesModel

class VariablesModel(models.Model):    
    id = models.BigAutoField(primary_key=True,db_column="var_id")
    nombre_variable = models.CharField("Variable name",max_length=255,null=False,blank=False,db_column="var_nombre")
    range_variable = models.IntegerField("Variable range",null=False,blank=False,db_column="var_range")
    valor_defecto = models.IntegerField("Variable valor ",null=False,blank=False,db_column="var_valor_defecto")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
            return super(VariablesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Variables'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_variable


class PruebaCalculoModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_id")
    pruebas_resultado = models.JSONField("Test results",null=False,blank=False,db_column="prb_cal_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_tolerancia")
    pruebas_condicion_respuesta = models.TextField("Test's condition",null=False,blank=False,db_column="prb_cal_condicion_respuesta")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    operacion = models.ManyToManyField(OperacionesModel,through="Prb_Calculo_Operacion_Model",through_fields=('calculo', 'operacion'))
    # operacion_relacion = models.ManyToManyField(OperacionesModel,through="Prb_Calculo_Operacion_Relacionada_Model",through_fields=('calculo', 'operacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
            return super(PruebaCalculoModel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaCalculo'
        
    def __str__(self):
        return str(self.id)

class PruebaOpcionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_opc_id")
    pruebas_opciones = models.JSONField("Test results",null=False,blank=False,db_column="prb_opc_resultado")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
            if not self.id:
                self.created_at = timezone.now()        
                return super(PruebaOpcionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaOpciones'
        
    def __str__(self):
        return str(self.id)

class PruebasModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_id")
    pruebas_titulo = models.CharField("Test name",max_length=255,null=False,blank=False,unique=True,db_column="prb_titulo")
    pruebas_contexto = models.TextField("Test context",null=True,blank=False,db_column="prb_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    
    calculo = models.ManyToManyField(PruebaCalculoModel,through="Prueba_Tipo_Model",through_fields=('prueba','calculo'))
    opcion = models.ManyToManyField(PruebaOpcionesModel,through="Prueba_Tipo_Model",through_fields=('prueba', 'opcion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
            return super(PruebasModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_Pruebas'
    
    def __str__(self):
        return str(self.id) + '-' + self.pruebas_titulo



class SeccionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="scc_id")
    secciones_titulo = models.CharField("Section name",max_length=255,null=False,blank=False,unique=True,db_column="scc_nombre")
    secciones_contexto = models.TextField("Section context",null=True,blank=False,db_column="scc_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    pruebas = models.ManyToManyField(PruebasModel,through="Scc_Prb_Model",through_fields=('seccion', 'prueba'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
            return super(SeccionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Secciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.secciones_titulo

class ProtocolsModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prt_id")
    protocolo_titulo = models.CharField("Protocol name",max_length=255,null=False,blank=False,unique=True,db_column="prt_nombre")
    protocolo_detalles = models.JSONField("Protocol details",editable=True,null=True,blank=False,db_column="prt_detalles")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    secciones = models.ManyToManyField(SeccionesModel,through="Prt_Scc_Model",through_fields=('protocolo', 'seccion'))
    variables = models.ManyToManyField(VariablesModel,through="Prt_Var_Model",through_fields=('protocolo', 'variables'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
            return super(ProtocolsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Protocolos'
    
    def __str__(self):
        return str(self.id) + '-' + self.protocolo_titulo




class Prueba_Tipo_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCal_id")
    prueba = models.ForeignKey(PruebasModel,on_delete=models.CASCADE)
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True,blank=False)
    opcion = models.ForeignKey(PruebaOpcionesModel,on_delete=models.CASCADE,null=True,blank=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prueba_Tipo_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_tipos'  

class Prb_Calculo_Operacion_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOpr_id")
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    variable = models.ManyToManyField(VariablesModel,through="Prb_Operacion_Variables",through_fields=('operacion', 'variables'))
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prb_Calculo_Operacion_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_calculo_operacion'  

class Prb_Calculo_Operacion_Relacionada_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOprRel_id")
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    variable = models.ManyToManyField(Prb_Calculo_Operacion_Model,through="Prb_OperacionRelacion_Operacion_Model",through_fields=('operacion_relacion', 'operacion'))
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prb_Calculo_Operacion_Relacionada_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_calculo_operacion_relacionada'  

class Prb_OperacionRelacion_Operacion_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbOprRel_id")
    operacion_relacion = models.ForeignKey(Prb_Calculo_Operacion_Relacionada_Model,on_delete=models.CASCADE)
    operacion = models.ForeignKey(Prb_Calculo_Operacion_Model,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prb_OperacionRelacion_Operacion_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_calculo_operacion_reacionada_operacion'  

class Prb_Operacion_Variables(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbOprVar_id")
    operacion = models.ForeignKey(Prb_Calculo_Operacion_Model,on_delete=models.CASCADE)
    variables = models.ForeignKey(VariablesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prb_Operacion_Variables, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_operacion_variables'  

class Prt_Scc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrtScc_id")
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prt_Scc_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_protocolo_secciones'

class Scc_Prb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="SccPrb_id")
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebasModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Scc_Prb_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_secciones_prueba'

class Prt_Var_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="Pr_id")
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    variables = models.ForeignKey(VariablesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(Prt_Var_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Protocolo_Variables'