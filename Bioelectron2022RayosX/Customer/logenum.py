class LogEnumOrganizaciones():
    ORGANIZACION_CREATED = 'Nueva organización creada por '
    ORGANIZACION_UPDATED = 'Organización actualizada por '
    ORGANIZACION_REMOVED = 'Organización removida por '
    ORGANIZACION_ENABLED = 'Organización inhabilitada por '

class LogEnumDepartamentos():
    DEPARTAMENTO_CREATED = 'Nuevo departamento creado por '
    DEPARTAMENTO_UPDATED = 'Departamento actualizado por '
    DEPARTAMENTO_REMOVED = 'Departamento removido por '
    DEPARTAMENTO_ENABLED = 'Departamento inhabilitado por '

class LogEnumAreas():
    AREA_CREATED = 'Nueva área creada por '
    AREA_UPDATED = 'Área actualizada por '
    AREA_REMOVED = 'Área removida por '
    AREA_ENABLED = 'Área inhabilitada por '


def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)


