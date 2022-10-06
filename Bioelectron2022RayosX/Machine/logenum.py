class LogEnumSistemas():
    SISTEMA_CREATED = 'Nuevo sistema creado por '
    SISTEMA_UPDATED = 'Sistema actualizado por '
    SISTEMA_REMOVED = 'Sistema removido por '
    SISTEMA_ENABLED = 'Sistema inhabilitado por '

class LogEnumTubos():
    TUBO_CREATED = 'Nuevo Tubo creado por '
    TUBO_UPDATED = 'Tubo actualizado por '
    TUBO_REMOVED = 'Tubo removido por '
    TUBO_ENABLED = 'Tubo inhabilitado por '

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)


