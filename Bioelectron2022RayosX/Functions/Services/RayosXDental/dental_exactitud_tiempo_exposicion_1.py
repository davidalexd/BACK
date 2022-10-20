from Functions.Services.promedio import promedio
def dental_exactitud_tiempo_exposicion_1(element,attribute):

    # llama TIEMPO DE EXPOSICIÓN (s) y luego a tiempo en rango de 5
    resultado =  [{"resultado":0}]
    element_1 = float(element[0])
    prom = promedio(attribute)
    operacion = (element_1-prom)/element_1

    redondeo=round(operacion,2)
    tolerancia_1 = 10
    tolerancia_2 = -10
    tolerancia = True

    if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado
