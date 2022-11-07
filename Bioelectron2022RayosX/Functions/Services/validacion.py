def validacion(attributes=[True]):
    validacion = True
    if False in attributes:
        validacion = False
    else:
        validacion = True
    
    return validacion
