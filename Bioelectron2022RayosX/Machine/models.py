from django.db import models

from simple_history.models import HistoricalRecords
from Base.models import BaseModel

from django.utils import timezone



class TuboModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="tb_id")
    title = models.CharField("Component title", max_length=255,null=False,blank=False,db_column="tb_title_componente")
    marca = models.CharField("Component brand", max_length=255,null=False,blank=False,db_column="tb_marca_componente")
    modelo = models.CharField("Component model", max_length=255,null=False,blank=False,db_column="tb_modelo_componente")
    antiguedad = models.DateField("Component's year",auto_now_add=False,null=True,blank=True,db_column="tb_antiguedad_tcomponente")
    year_instalacion = models.DateField("Component's installation",auto_now_add=False,null=True,blank=True,db_column="tb_year_componente")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(TuboModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

    @property
    def name_option(self):
        return self.title + '-' + self.marca + '-' + self.modelo + '-'

    class Meta:
        ordering = ["id"]
        db_table = 'machines_Tubos'
    
    def __str__(self):
        return str(self.id)+ self.title + '-' + self.marca + '-' + self.modelo

class SistemaModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="stm_id")
    title = models.CharField("System title", max_length=255,null=False,blank=False,db_column="stm_title_sistema")
    marca = models.CharField("System brand", max_length=255,null=False,blank=False,db_column="stm_marca_sistema")
    modelo = models.CharField("System model", max_length=255,null=False,blank=False,db_column="stm_modelo_sistema")
    antiguedad = models.DateField("System's year",auto_now_add=False,null=True,blank=True,db_column="stm_antiguedad_sistema")
    year_instalacion = models.DateField("System's nstallation",auto_now_add=False,null=True,blank=True,db_column="stm_year_sistema")
    members = models.ManyToManyField(TuboModel,through="Stm_Tb_Model",through_fields=('sistema', 'tubo'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(SistemaModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

    @property
    def name_option(self):
        return self.title+ '-' +self.marca + '-' + self.modelo + '-'

    class Meta:
        ordering = ["id"]
        db_table = 'machines_Sistemas'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo




class Stm_Tb_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="StmTb_id")
    sistema = models.ForeignKey(SistemaModel,on_delete=models.CASCADE)
    tubo = models.ForeignKey(TuboModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=False)

    class Meta:
        ordering = ["id"]
        db_table = 'reports_sistemas_tubos'
