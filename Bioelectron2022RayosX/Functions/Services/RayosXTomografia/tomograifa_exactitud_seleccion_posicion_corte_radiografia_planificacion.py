def tomograifa_exactitud_seleccion_posicion_corte_radiografia_planificacion(element):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    tolerancia =True
    redondear = round(float(element[0]),2)
    
    tolerancia_1 = 2
    tolerancia_2 = -2

    if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado
