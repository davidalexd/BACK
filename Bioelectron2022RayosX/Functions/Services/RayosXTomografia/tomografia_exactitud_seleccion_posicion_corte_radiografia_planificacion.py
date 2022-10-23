def tomograifa_exactitud_seleccion_posicion_corte_radiografia_planificacion(element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia =True
    redondear = round(float(element[0]),2)
    
    tolerancia_1 = 2
    tolerancia_2 = -2

    if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":""}

    return resultado
