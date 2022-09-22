from django.db import models
from django.utils import timezone

class OperacionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="InpFs_id")
    operacion_titulo = models.CharField("Operation's title", max_length=255,null=False,blank=False,unique=True,db_column="opr_titulo")
    operacion_funcion= models.CharField("Operation's function", max_length=255,null=False,blank=False,unique=True,db_column="opr_funcion")
    operacion_contexto = models.TextField("Operation's context", max_length=255,null=False,blank=False,unique=True,db_column="opr_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(OperacionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Operaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.operacion_titulo