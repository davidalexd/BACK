class LogEnumProtocolos():
    PROTOCOLO_CREATED = 'Nueva protocolo creado por '
    PROTOCOLO_UPDATED = 'Protocolo actualizado por '
    PROTOCOLO_REMOVED = 'Protocolo removido por '
    PROTOCOLO_ENABLED = 'Protocolo inhabilitado por '

class LogEnumSecciones():
    SECCION_CREATED = 'Nueva sección creada por '
    SECCION_UPDATED = 'Sección actualizada por '
    SECCION_REMOVED = 'Sección removida por '
    SECCION_ENABLED = 'Sección inhabilitada por '

class LogEnumPruebaCalculo():
    PRUEBA_CALCULO_CREATED = 'Nueva prueba calculo creada por '
    PRUEBA_CALCULO_UPDATED = 'Prueba calculo actualizada por '
    PRUEBA_CALCULO_REMOVED = 'Prueba calculo removida por '
    PRUEBA_CALCULO_ENABLED = 'Prueba calculo inhabilitada por '

class LogEnumPruebaOpciones():
    PRUEBA_OPCION_CREATED = 'Nueva prueba opción creada por '
    PRUEBA_OPCION_UPDATED = 'Prueba opción actualizada por '
    PRUEBA_OPCION_REMOVED = 'Prueba opción removida por '
    PRUEBA_OPCION_ENABLED = 'Prueba opción inhabilitada por '

class LogEnumVariables():
    VARIABLE_CREATED = 'Nueva variable creada por '
    VARIABLE_UPDATED = 'Variable actualizada por '
    VARIABLE_REMOVED = 'Variable removida por '
    VARIABLE_ENABLED = 'Variable inhabilitada por '

def OrganizacionLog(author,instance,message,relacion):
    relacion.objects.create(model=instance,model_user=author.request.user,context=message+author.request.user.username)


