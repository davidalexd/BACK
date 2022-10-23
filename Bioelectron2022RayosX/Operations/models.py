from email.policy import default
from enum import unique
from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone


class VariablesModel(BaseModel):    
    id = models.BigAutoField(primary_key=True,db_column="var_id")
    nombre_variable = models.CharField("Variable name",max_length=255,null=False,blank=False,unique=False,db_column="var_nombre")
    range_variable = models.IntegerField("Variable range",null=False,blank=False,db_column="var_range")
    valor_defecto = models.JSONField("Variable valor ",null=True,blank=True,db_column="var_valor_defecto")
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(VariablesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Variables'
    
    def __str__(self):
        return str(self.id) + '-' + self.nombre_variable

class OperacionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="opr_id")
    operacion_titulo = models.CharField("Operation's title", max_length=255,null=False,blank=False,unique=False,db_column="opr_titulo")
    operacion_funcion= models.CharField("Operation's function", max_length=255,null=False,blank=False,unique=True,db_column="opr_funcion")
    operacion_symbol= models.CharField("Operation's symbol",max_length=255,null=True,blank=True,unique=True,db_column="opr_simbolo")
    operacion_variable= models.IntegerField("Operation's number of variables",default=1,null=False,blank=False,db_column="opr_cantidad_variables")
    operacion_contexto = models.TextField("Operation's context", max_length=255,null=False,blank=True,db_column="opr_contexto")
    variables = models.ManyToManyField(VariablesModel,through="Opr_Operacion_Variables",through_fields=('operacion', 'variables'))
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(OperacionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Operaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.operacion_titulo + " .:: " + str(self.operacion_symbol) + " ::. " + "["+ str(self.operacion_variable) +"]"

class CategoryOperacionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="cat_opr_id")
    category_operacion_titulo = models.CharField("Category's title", max_length=255,null=False,blank=False,unique=False,db_column="cat_opr_titulo")
    category_operacion_contexto = models.TextField("Operation's context", max_length=255,null=True,blank=True,db_column="cat_opr_contexto")
    operaciones = models.ManyToManyField(OperacionesModel,through="Cat_Category_Operaciones",through_fields=('categoria','operacion'))
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(CategoryOperacionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Categorias_Operaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.category_operacion_titulo

class Cat_Category_Operaciones(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="CatOpr_id")
    categoria = models.ForeignKey(CategoryOperacionesModel,on_delete=models.CASCADE)
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'categoria_operaciones'  

class Opr_Operacion_Variables(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="OprVar_id")
    operacion = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    variables = models.ForeignKey(VariablesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'operacion_variables'  