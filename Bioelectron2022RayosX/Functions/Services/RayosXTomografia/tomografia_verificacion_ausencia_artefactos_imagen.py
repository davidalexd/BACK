def tomografia_verificacion_ausencia_artefactos_imagen(opcion=""):
    resultado = [{"parametros":"","resultado":"","condicion":True}]
    tolerancia = True

    if(opcion[0]=="Ausencia de artefactos"):
        tolerancia = True  
    else:
        toleranci = False
    
    return resultado = [{"parametros":"","resultado":opcion,"condicion":tolerancia}]


