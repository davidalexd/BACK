from django.db import models
from django.utils import timezone

class InspeccionesFisicasModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="InpFs_id")
    inspeccion_fisica_titulo = models.CharField("Physical inspection title", max_length=255,null=False,blank=False,unique=True,db_column="InpFs_name")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(InspeccionesFisicasModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_InpeccionesFisicas'
    
    def __str__(self):
        return str(self.id) + '-' + self.inspeccion_fisica_titulo