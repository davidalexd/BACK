from Functions.Services.promedio import promedio

def dental_exactitud_tension(element,attribute):
    # llama TENSION NOMINAL  (kV) luego a TENSION PROMEDIO (kV) range (5)
    resultado = [{"resultado":0}]
    prom = promedio(attribute)
    element_1 = float(element[0])

    operacion = (element_1-prom)/element_1
    redondear = round((operacion)*100,2)

    tolerancia_1 = 10
    tolerancia = True

    if (redondear < tolerancia_1*2 or element < tolerancia_1):
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