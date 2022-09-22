from django.db import models
from django.utils import timezone
from Operations.models import OperacionesModel

class PruebaCalculoRelacion(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_rel_id")
    variable = models.JSONField("Test variable",null=False,blank=False,db_column="prb_cal_rel_variable")
    pruebas_resultado = models.JSONField("Test results",null=False,blank=False,db_column="prb_cal_rel_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_rel_tolerancia")
    pruebas_condicion_respuesta = models.TextField("Test's condition",null=False,blank=False,db_column="prb_cal_rel_condicion_respuesta")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    operaciones = models.ManyToManyField(OperacionesModel,through="Prb_Cal_Opr_Model",through_fields=('calculo_relacion', 'operacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(PruebaCalculoRelacion, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaCalculoRelacion'
        
    def __str__(self):
        return str(self.id)

class PruebaCalculo(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_id")
    variable = models.JSONField("Test variable",null=False,blank=False,db_column="prb_cal_variable")
    pruebas_resultado = models.JSONField("Test results",null=False,blank=False,db_column="prb_cal_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_tolerancia")
    pruebas_condicion_respuesta = models.TextField("Test's condition",null=False,blank=False,db_column="prb_cal_condicion_respuesta")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    operaciones = models.ManyToManyField(OperacionesModel,through="Prb_Cal_Opr_Model",through_fields=('calculo', 'operacion'))
    prueba_relacion = models.ManyToManyField(PruebaCalculoRelacion,through="Prb_PrbRelacion_Model",through_fields=('prueba_calculo', 'prueba_relacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(PruebaCalculo, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaCalculo'
        
    def __str__(self):
        return str(self.id)

class PruebaOpciones(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prb_opc_id")
    pruebas_opciones = models.JSONField("Test results",null=False,blank=False,db_column="prb_opc_resultado")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
            if not self.id:
                self.crated_at = timezone.now()        
                return super(PruebaOpciones, self).save(*args, **kwargs)

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
    
    calculo = models.ManyToManyField(PruebaCalculo,through="Prb_Calculo_Model",through_fields=('prueba','calculo'))
    calculo_relacion = models.ManyToManyField(PruebaCalculoRelacion,through="Prb_Calculo_Model",through_fields=('prueba','calculo_relacion'))
    opcion = models.ManyToManyField(PruebaOpciones,through="Prb_Calculo_Model",through_fields=('prueba', 'opcion'))

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
    prueba_calculo = models.ForeignKey(PruebaCalculo,on_delete=models.CASCADE)
    prueba_relacion = models.ForeignKey(PruebaCalculoRelacion,on_delete=models.CASCADE)
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
    calculo = models.ForeignKey(PruebaCalculo,on_delete=models.CASCADE)
    calculo_relacion = models.ForeignKey(PruebaCalculoRelacion,on_delete=models.CASCADE)
    opcion = models.ForeignKey(PruebaOpciones,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Calculo_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_calculo'
        
class Prb_Cal_Opr_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOpr_id")
    calculo = models.ForeignKey(PruebaCalculo,on_delete=models.CASCADE)
    calculo_relacion = models.ForeignKey(PruebaCalculoRelacion,on_delete=models.CASCADE)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prb_Cal_Opr_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_calculo_operaciones'