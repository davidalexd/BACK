from Functions.Services.promedio import promedio

def tomografia_filtracion_capa_hemirreductora(element_1,attribute,element_2):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    prom = promedio(attribute)
    tolerancia = True
    operacion = float(element_1[0])-prom-float(element_2[0])
    redondear = round(operacion,2)
    tolerancia_1 = 1
    tolerancia_2 = -1

    if (redondear <= tolerancia_1 or redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
        {
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        }
    ]
    
    return resultado
