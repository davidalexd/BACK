from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_rendimiento(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    des_v = desviacion_estandar_m(attributes)
    tolerancia = True
    if (prom == 0):
        operacion = 0
    else:
        operacion = des_v/prom   
    redondear = round(operacion,2)

    if(redondear<10):
        tolerancia = True
    else:
        tolerancia = False   
    
    resultado = [{
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
            }]
    return resultado
