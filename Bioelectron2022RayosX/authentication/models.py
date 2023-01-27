from django.db import models
from Base.models import BaseModel
from User.models import User
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class SesionesModel(BaseModel):
    id = models.BigAutoField(primary_key=True,db_column="ss_id")
    ubicacion = models.JSONField(null=True,db_column="ss_ubicacion")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(SesionesModel, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["id"]
        db_table = 'authenticacion_Sesiones'
    