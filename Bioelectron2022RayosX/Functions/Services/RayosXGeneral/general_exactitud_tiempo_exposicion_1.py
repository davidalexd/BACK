def general_exactitud_tiempo_exposicion_1(element_1,element_2):
    resultado = [{"resultado":0}]
    operacion = (element_1[0]-element_2[0])/element_2[0]
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado