from django.db import models
from django.utils import timezone

class SistemaModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="stm_id")
    marca = models.CharField("System brand", max_length=255,null=False,blank=False,db_column="stm_marca_sistema")
    modelo = models.CharField("System model", max_length=255,null=False,blank=False,db_column="stm_modelo_sistema")
    serie = models.CharField("System series", max_length=255,null=False,blank=False,unique=True,db_column="stm_serie_sistema")
    antiguedad = models.DateField("System's year",auto_now_add=False,null=True,blank=True,db_column="stm_antiguedad_sistema")
    year_instalacion = models.DateField("System's nstallation",auto_now_add=False,null=True,blank=True,db_column="stm_year_sistema")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(SistemaModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

    class Meta:
        ordering = ["id"]
        db_table = 'machines_Sistemas'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo


class TuboModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="stm_id")
    marca = models.CharField("Tube brand", max_length=255,null=False,blank=False,db_column="tb_marca_tubo")
    modelo = models.CharField("Tube model", max_length=255,null=False,blank=False,db_column="tb_modelo_tubo")
    serie = models.CharField("Tube series", max_length=255,null=False,blank=False,unique=True,db_column="tb_serie_tubo")
    antiguedad = models.DateField("Tube's year",auto_now_add=False,null=True,blank=True,db_column="tb_antiguedad_tubo")
    year_instalacion = models.DateField("Tube's installation",auto_now_add=False,null=True,blank=True,db_column="tb_year_tubo")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(TuboModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

    class Meta:
        ordering = ["id"]
        db_table = 'machines_Tubos'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo