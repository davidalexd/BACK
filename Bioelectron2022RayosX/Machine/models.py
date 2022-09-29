from django.db import models
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL



class TuboModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="tb_id")
    marca = models.CharField("Tube brand", max_length=255,null=False,blank=False,db_column="tb_marca_tubo")
    modelo = models.CharField("Tube model", max_length=255,null=False,blank=False,db_column="tb_modelo_tubo")
    serie = models.CharField("Tube series", max_length=255,null=False,blank=False,unique=True,db_column="tb_serie_tubo")
    antiguedad = models.DateField("Tube's year",auto_now_add=False,null=True,blank=True,db_column="tb_antiguedad_tubo")
    year_instalacion = models.DateField("Tube's installation",auto_now_add=False,null=True,blank=False,db_column="tb_year_tubo")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    users = models.ManyToManyField(User,through="User_tubos_Model",through_fields=('model', 'model_user'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(TuboModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

    class Meta:
        ordering = ["id"]
        db_table = 'machines_Tubos'
    
    def __str__(self):
        return str(self.id) + '-' + self.marca + '-' + self.modelo

class SistemaModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="stm_id")
    marca = models.CharField("System brand", max_length=255,null=False,blank=False,db_column="stm_marca_sistema")
    modelo = models.CharField("System model", max_length=255,null=False,blank=False,db_column="stm_modelo_sistema")
    serie = models.CharField("System series", max_length=255,null=False,blank=False,unique=True,db_column="stm_serie_sistema")
    antiguedad = models.DateField("System's year",auto_now_add=False,null=True,blank=True,db_column="stm_antiguedad_sistema")
    year_instalacion = models.DateField("System's nstallation",auto_now_add=False,null=True,blank=True,db_column="stm_year_sistema")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    members = models.ManyToManyField(TuboModel,through="Stm_Tb_Model",through_fields=('sistema', 'tubo'))
    users = models.ManyToManyField(User,through="User_sistemas_Model",through_fields=('model', 'model_user'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(SistemaModel, self).save(*args, **kwargs)

    @property
    def antiguedad_year(self):
        return self.antiguedad.strftime('%Y')

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
    

class User_sistemas_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(SistemaModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_sistemas_Model, self).save(*args, **kwargs)

class User_tubos_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(TuboModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_tubos_Model, self).save(*args, **kwargs)