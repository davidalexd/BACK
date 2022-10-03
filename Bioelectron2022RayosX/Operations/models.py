from django.db import models
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL


class OperacionesModel(models.Model):
    id = models.BigAutoField(primary_key=True,db_column="InpFs_id")
    operacion_titulo = models.CharField("Operation's title", max_length=255,null=False,blank=False,unique=True,db_column="opr_titulo")
    operacion_funcion= models.CharField("Operation's function", max_length=255,null=False,blank=False,unique=True,db_column="opr_funcion")
    operacion_symbol= models.CharField("Operation's symbol",max_length=255,null=True,blank=True,unique=True,db_column="opr_simbolo")
    operacion_contexto = models.TextField("Operation's context", max_length=255,null=False,blank=True,db_column="opr_contexto")
    is_enabled = models.BooleanField(default=True,null=False)
    created_at = models.DateTimeField(editable=False,null=False,blank=False)
    users = models.ManyToManyField(User,through="User_Operaciones_Model",through_fields=('model', 'model_user'))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()        
        return super(OperacionesModel, self).save(*args, **kwargs)

    class Meta:
        ordering = ["id"]
        db_table = 'operations_Operaciones'
    
    def __str__(self):
        return str(self.id) + '-' + self.operacion_titulo + " .:: " + self.operacion_symbol + " ::. " 

    
class User_Operaciones_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(OperacionesModel,on_delete=models.CASCADE)
    model_user = models.ForeignKey(User,on_delete=models.CASCADE)
    context = models.TextField()
    registerd_at = models.DateTimeField(editable=False,null=False,blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.registerd_at = timezone.now()        
        return super(User_Operaciones_Model, self).save(*args, **kwargs)



