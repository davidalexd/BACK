from django.db import models
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL

class CalibracionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="cal_id")
    fecha_calibracion = models.DateField("Calibration date",auto_now_add=False,null=False,blank=False,db_column="cal_fecha_calibracion")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    user = models.ManyToManyField(User,through="User_Calibraciones_Model",through_fields=('model', 'model_user'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
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
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    members = models.ManyToManyField(CalibracionesModel,through="Cal_Med_Model",through_fields=('medidor', 'calibracion'))
    user = models.ManyToManyField(User,through="User_Medidores_Model",through_fields=('model', 'model_user'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(MedidoresModel, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.marca+' '+' '+self.modelo+' '+self.serie

    class Meta:
        ordering = ["id"]
        db_table = 'companymachine_Medidores'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo



class Cal_Med_Model(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="CalMed_id")
    medidor = models.ForeignKey(MedidoresModel,on_delete=models.CASCADE)
    calibracion = models.ForeignKey(CalibracionesModel,on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False,default=timezone.now,null=False,blank=True)

    class Meta:
        ordering = ["id"]
        db_table = 'companymachine_calibraciones_medidores'



class User_Medidores_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(MedidoresModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Medidores_Model, self).save(*args, **kwargs)

class User_Calibraciones_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(CalibracionesModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Calibraciones_Model, self).save(*args, **kwargs)