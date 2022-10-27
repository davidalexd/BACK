from django.db import models
from simple_history.models import HistoricalRecords
from User.models import User

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    is_enabled = models.BooleanField('Estado',default=True,null=False)
    created_at = models.DateField('Fecha de Creación',auto_now=False, auto_now_add = True)
    updated_at = models.DateField('Fecha de Modificacion',auto_now=True, auto_now_add = False)
    deleted_at = models.DateField('Fecha de Eliminación',auto_now=True, auto_now_add = False)
    historical = HistoricalRecords(User,inherit=True)

    @property 
    def _history_user(self):
        return self.changed_by

    @_history_user.setter 
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'