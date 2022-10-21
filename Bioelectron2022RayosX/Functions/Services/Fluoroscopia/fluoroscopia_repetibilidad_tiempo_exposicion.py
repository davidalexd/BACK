from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_tiempo_exposicion(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    des_v = desviacion_estandar_m(attributes)
    
    tolerancia = True

    if (prom == 0):
        operacion = 0
    else:
        operacion = (des_v/prom)*100

    redondear = round(operacion,2)
    if(redondear < 10):
        tolerancia = True
    else:
        tolerancia = False
        
    resultado = [{
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
            }]
    return resultado