from django.db import models
from django.utils import timezone
from Tests.models import PruebasModel

class SeccionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="scc_id")
    secciones_titulo = models.CharField("Section name",max_length=255,null=False,blank=False,unique=True,db_column="scc_nombre")
    secciones_contexto = models.TextField("Section context",null=True,blank=True,db_column="scc_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    pruebas = models.ManyToManyField(PruebasModel,through="Scc_Prb_Model",through_fields=('seccion', 'prueba'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(SeccionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Secciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.secciones_titulo

class ProtocolsModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prt_id")
    protocolo_titulo = models.CharField("Protocol name",max_length=255,null=False,blank=False,unique=True,db_column="prt_nombre")
    protocolo_detalles = models.JSONField("Protocol details",editable=True,null=True,blank=True,db_column="prt_detalles")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    secciones = models.ManyToManyField(SeccionesModel,through="Prt_Scc_Model",through_fields=('protocolo', 'seccion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(ProtocolsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Protocolos'
    
    def __str__(self):
        return str(self.id) + '-' + self.protocolo_titulo


class Prt_Scc_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="PrtScc_id")
    protocolo = models.ForeignKey(ProtocolsModel,on_delete=models.CASCADE)
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Prt_Scc_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_protocolo_secciones'

class Scc_Prb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="SccPrb_id")
    seccion = models.ForeignKey(SeccionesModel,on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebasModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Scc_Prb_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_secciones_prueba'

