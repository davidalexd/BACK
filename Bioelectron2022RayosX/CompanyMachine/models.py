from django.db import models
from django.utils import timezone


class CalibracionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="cal_id")
    fecha_calibracion = models.DateField("Calibration date",auto_now_add=False,null=False,blank=False,db_column="cal_fecha_calibracion")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(CalibracionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'companymachine_Calibraciones'
    
    def __str__(self):
        return str(self.id) + '-' + str(self.fecha_calibracion)


class MedidoresModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="med_id")
    marca = models.CharField("Meter brand", max_length=255,null=False,blank=False,db_column="med_marca_medidor")
    modelo = models.CharField("Meter model", max_length=255,null=False,blank=False,db_column="med_modelo_medidor")
    serie = models.CharField("Meter series", max_length=255,null=False,blank=False,unique=True,db_column="med_serie_medidor")
    is_enabled = models.BooleanField(default=True,null=False)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)
    members = models.ManyToManyField(CalibracionesModel,through="Cal_Med_Model",through_fields=('medidor', 'calibracion'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
            return super(MedidoresModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'companymachine_Medidores'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo



class Cal_Med_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="CalMed_id")
    medidor = models.ForeignKey(MedidoresModel,on_delete=models.CASCADE)
    calibracion = models.ForeignKey(CalibracionesModel,on_delete=models.CASCADE)
    crated_at = models.DateTimeField(editable=False,null=False,blank=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.crated_at = timezone.now()        
        return super(Cal_Med_Model, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'companymachine_calibraciones_medidores'