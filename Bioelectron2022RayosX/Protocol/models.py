from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone

from Operations.models import OperacionesModel




class PruebaCalculoModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="prb_cal_id")
    pruebas_titulo = models.CharField("Test name",max_length=255,null=False,blank=False,unique=False,db_column="prb_cal_titulo")
    pruebas_contexto = models.TextField("Test context",null=True,blank=True,db_column="prb_cal_contexto")
    pruebas_resultado = models.TextField("Test results",null=True,blank=True,db_column="prb_cal_resultado")
    pruebas_tolerancia = models.TextField("Test's tolerance",null=False,blank=False,db_column="prb_cal_tolerancia")
    pruebas_condicion_respuesta = models.JSONField("Test's condition",null=False,blank=False,db_column="prb_cal_condicion_respuesta")
    operacion = models.ManyToManyField(OperacionesModel,through="Prb_Calculo_Operacion_Model",through_fields=('calculo', 'operacion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(PruebaCalculoModel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaCalculo'
        
    def __str__(self):
        return str(self.id) + "-" + self.pruebas_titulo

class PruebaOpcionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="prb_opc_id")
    pruebas_titulo = models.CharField("Test name",max_length=255,null=False,blank=False,unique=False,db_column="prb_opc_titulo")
    pruebas_contexto = models.TextField("Test context",null=True,blank=True,db_column="prb_opc_contexto")
    pruebas_opciones = models.JSONField("Test results",null=False,blank=False,db_column="prb_opc_resultado")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(PruebaOpcionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_PruebaOpciones'
        
    def __str__(self):
        return str(self.id) + "-" + self.pruebas_titulo



class SeccionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="scc_id")
    secciones_titulo = models.CharField("Section name",max_length=255,null=False,blank=False,unique=False,db_column="scc_nombre")
    secciones_contexto = models.TextField("Section context",null=True,blank=True,db_column="scc_contexto")

    calculo = models.ManyToManyField(PruebaCalculoModel,through="Prueba_Tipo_Model",through_fields=('seccion','calculo'))
    opcion = models.ManyToManyField(PruebaOpcionesModel,through="Prueba_Tipo_Model",through_fields=('seccion', 'opcion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(SeccionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Secciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.secciones_titulo

class ProtocolsModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="prt_id")
    protocolo_titulo = models.CharField("Protocol name",max_length=255,null=False,blank=False,unique=True,db_column="prt_nombre")
    protocolo_detalles = models.JSONField("Protocol details",editable=True,null=True,blank=False,db_column="prt_detalles")
    secciones = models.ManyToManyField(SeccionesModel,through="Prt_Scc_Model",through_fields=('protocolo', 'seccion'))

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
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True,blank=True)
    opcion = models.ForeignKey(PruebaOpcionesModel,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_prueba_tipos'  

class Prb_Calculo_Operacion_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrbCalOpr_id")
    calculo = models.ForeignKey(PruebaCalculoModel,on_delete=models.CASCADE,null=True)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'tests_calculo_operacion'  


class Prt_Scc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrtScc_id")
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_protocolo_secciones'


