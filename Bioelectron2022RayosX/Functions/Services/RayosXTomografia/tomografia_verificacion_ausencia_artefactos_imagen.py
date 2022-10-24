def tomografia_verificacion_ausencia_artefactos_imagen(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True

    if(opcion[0]=="Ausencia de artefactos"):
        tolerancia = True  
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":opcion,"condicion":tolerancia}],"tolerancia":"No se deben apreciar artefactos en las imágenes de tomografía."}

    return resultado


