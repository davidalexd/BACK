from desviacion_estandar_m import desviacion_estandar_m
from promedio import promedio as prom

def repetibilidad_tension(attributes):
    desviacion_estandar = desviacion_estandar_m(attributes)
    promedio = prom(attributes)
    repetibilidad_tension = desviacion_estandar/promedio
    resultado = {"valor":repetibilidad_tension}
    return resultado