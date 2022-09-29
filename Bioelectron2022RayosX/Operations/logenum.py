class LogEnumOperaciones():
    OPERACION_CREATED = 'Nueva operación creada por '
    OPERACION_UPDATED = 'Operación actualizada por '
    OPERACION_REMOVED = 'Operación removida por '
    OPERACION_ENABLED = 'Operación inhabilitada por '

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)


