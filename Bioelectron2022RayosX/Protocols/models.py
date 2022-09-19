from django.db import models
from django.utils import timezone

class ProtocolsModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="prt_id")
    nombre_protocolo = models.CharField("Tube brand", max_length=255,null=False,blank=False,unique=True,db_column="prt_name")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(ProtocolsModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'protocols_Protocolos'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_protocolo