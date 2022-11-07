from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio as prom

def coeficiente_variacion(attributes):
    promedio = prom(attributes)
    desviacion_estandar = desviacion_estandar_m(attributes)

    coeficiente_variacion = desviacion_estandar/promedio
    resultado = coeficiente_variacion
    return resultado