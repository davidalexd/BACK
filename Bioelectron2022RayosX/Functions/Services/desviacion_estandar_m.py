
from Functions.Services.promedio import promedio as prom
import numpy as np

def desviacion_estandar_m(attributes):
    promedio = prom(attributes)
    desviacion_estandar = 0
    for i in range(0,len(attributes)):
        desviacion_estandar = desviacion_estandar + (attributes[i]-promedio)**2
    desviacion_estandar = desviacion_estandar/(len(attributes)-1)
    desviacion_estandar = np.sqrt(desviacion_estandar)
    resultado = desviacion_estandar
    return resultado
