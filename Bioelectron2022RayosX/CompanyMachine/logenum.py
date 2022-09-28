class LogEnumCalibraciones():
    CALIBRACION_CREATED = 'Nueva calibración creada por '
    CALIBRACION_UPDATED = 'Calibracion actualizada por '
    CALIBRACION_REMOVED = 'Calibracion removida por '
    CALIBRACION_ENABLED = 'Calibracion inhabilitada por '

class LogEnumMedidores():
    MEDIDOR_CREATED = 'Nueva medidor creada por '
    MEDIDOR_UPDATED = 'Medidor actualizada por '
    MEDIDOR_REMOVED = 'Medidor removida por '
    MEDIDOR_ENABLED = 'Medidor inhabilitada por '

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)

