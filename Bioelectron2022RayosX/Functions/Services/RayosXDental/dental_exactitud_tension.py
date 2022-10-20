from Functions.Services.promedio import promedio

def dental_exactitud_tension(element,attribute):
    # llama TENSION NOMINAL  (kV) luego a TENSION PROMEDIO (kV) range (5)
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    prom = promedio(attribute)
    element_1 = float(element[0])

    if(element_1 <= 0):
        operacion=0*100
    else:
        operacion = ((element_1-prom)/element_1)*100
    redondear = round(operacion,2)

    tolerancia_1 = 10
    tolerancia_2 = -10

    if (redondear < tolerancia_1 or redondear < tolerancia_2):
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