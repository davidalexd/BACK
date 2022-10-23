def tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = float(element_1[0])+float(element_2[0])
    tolerancia =True
    redondear = round(operacion,2)
    
    if(redondear <= 2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"La distancia entre el plano indicado por las luces interna y externa y el plano de irradiación debe ser ≤ ±2 mm."}

    return resultado