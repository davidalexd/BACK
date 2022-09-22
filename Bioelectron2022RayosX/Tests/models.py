from pydoc import classname
from django.db import models
from django.utils import timezone
from Operations.models import OperacionesModel


class PruebaVariableModel(models.Model):
    id= models.BigAutoField(primary_key=True,db_column="var_id")
    nombre_variable = models.CharField("Nombre de la variable",max_length=255,null=False,blank=False,db_column="var_nombre")
    rango_variable = models.IntegerField("Rango de valores que puede tomar esta variable",null=False,blank=False,db_column="var_rango")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(PruebaVariableModel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaVariables'
        
    def __str__(self):
        return str(self.id) + '-' + self.nombre_variable

class PruebaCalculoRelacionModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_rel_id")
    pruebas_resultado = models.JSONField("Test results",null=False,blank=False,db_column="prb_cal_rel_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_rel_tolerancia")
    pruebas_condicion_respuesta = models.TextField("Test's condition",null=False,blank=False,db_column="prb_cal_rel_condicion_respuesta")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    operacion = models.ManyToManyField(OperacionesModel,through="Prb_Cal_Opr_Model",through_fields=('calculo_relacion', 'operacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(PruebaCalculoRelacionModel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaCalculoRelacion'
        
    def __str__(self):
        return str(self.id)

class PruebaCalculoModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_id")
    pruebas_resultado = models.JSONField("Test results",null=False,blank=False,db_column="prb_cal_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_tolerancia")
    pruebas_condicion_respuesta = models.TextField("Test's condition",null=False,blank=False,db_column="prb_cal_condicion_respuesta")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    prueba_relacion = models.ManyToManyField(PruebaCalculoRelacionModel,through="Prb_PrbRelacion_Model",through_fields=('prueba_calculo', 'prueba_relacion'))
    operacion = models.ManyToManyField(OperacionesModel,through="Prb_Cal_Opr_Model",through_fields=('calculo', 'operacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
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
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
            if not self.id:
                self.crated_at = timezone.now()        
                return super(PruebaOpcionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaOpciones'
        
    def __str__(self):
        return str(self.id)

class PruebasModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_id")
    pruebas_titulo = models.CharField("Test name",max_length=255,null=False,blank=False,unique=True,db_column="prb_titulo")
    pruebas_contexto = models.TextField("Test context",null=True,blank=True,db_column="prb_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    
    calculo = models.ManyToManyField(PruebaCalculoModel,through="Prb_Calculo_Model",through_fields=('prueba','calculo'))
    calculo_relacion = models.ManyToManyField(PruebaCalculoRelacionModel,through="Prb_Calculo_Model",through_fields=('prueba','calculo_relacion'))
    opcion = models.ManyToManyField(PruebaOpcionesModel,through="Prb_Calculo_Model",through_fields=('prueba', 'opcion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(PruebasModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_Pruebas'
    
    def __str__(self):
        return str(self.id) + '-' + self.pruebas_titulo


class Prb_PrbRelacion_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbPrbRl_id")
    prueba_calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE)
    prueba_relacion = models.ForeignKey(PruebaCalculoRelacionModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_PrbRelacion_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_prueba_calculo_relacion'

class Prb_Calculo_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCal_id")
    prueba = models.ForeignKey(PruebasModel,on_delete=models.CASCADE)
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True,blank=True)
    calculo_relacion = models.ForeignKey(PruebaCalculoRelacionModel,on_delete=models.CASCADE,null=True,blank=True)
    opcion = models.ForeignKey(PruebaOpcionesModel,on_delete=models.CASCADE,null=True,blank=True)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Calculo_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_tipos'  
  
class Prb_Cal_Opr_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOpr_id")
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True,blank=True)
    calculo_relacion = models.ForeignKey(PruebaCalculoRelacionModel,on_delete=models.CASCADE,null=True,blank=True)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    variables = models.ManyToManyField(PruebaVariableModel,through="Prb_Cal_Opr_Val_Model",through_fields=('operaciones_calculo', 'variable'))
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Cal_Opr_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_calculo_operaciones'

class Prb_Cal_Opr_Val_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOpr_id")
    operaciones_calculo = models.ForeignKey(Prb_Cal_Opr_Model,on_delete=models.CASCADE)
    variable = models.ForeignKey(PruebaVariableModel,on_delete=models.CASCADE)
    # operaciones_relacion = models.ForeignKey(Prb_Cal_Opr_Model,through="Prb_Cal_Opr_relacion_Val_Model",through_fields=('operacion_nueva', 'operacion_echa'))
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Cal_Opr_Val_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_calculo_operaciones_variables'


class Prb_Cal_Opr_relacion_Val_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOprRelVal_id")
    operacion_nueva = models.ForeignKey(Prb_Cal_Opr_Val_Model,on_delete=models.CASCADE)
    operacion_echa = models.ForeignKey(Prb_Cal_Opr_Model,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Cal_Opr_relacion_Val_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_calculo_operacion_relacion_variables'