from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone


class OperacionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="InpFs_id")
    operacion_titulo = models.CharField("Operation's title", max_length=255,null=False,blank=False,unique=True,db_column="opr_titulo")
    operacion_funcion= models.CharField("Operation's function", max_length=255,null=False,blank=False,unique=True,db_column="opr_funcion")
    operacion_symbol= models.CharField("Operation's symbol",max_length=255,null=True,blank=True,unique=True,db_column="opr_simbolo")
    operacion_variable= models.IntegerField("Operation's number of variables",default=1,null=False,blank=False,db_column="opr_cantidad_variables")
    operacion_contexto = models.TextField("Operation's context", max_length=255,null=False,blank=True,db_column="opr_contexto")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(OperacionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Operaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.operacion_titulo + " .:: " + str(self.operacion_symbol) + " ::. " + "["+ str(self.operacion_variable) +"]"

