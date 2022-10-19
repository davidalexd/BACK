from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_tiempo_exposicion(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    des_v = desviacion_estandar_m(attributes)
    if (prom == 0):
        operacion = 0
    else:
        operacion = (des_v/prom)*100

        
    redondear = round(operacion,2)
    resultado = [{"resultado":redondear,"decorador":"%"}]
    return resultado