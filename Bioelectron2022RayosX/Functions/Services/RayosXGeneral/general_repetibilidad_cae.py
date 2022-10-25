from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def general_repetibilidad_cae(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    desv = desviacion_estandar_m(attribute)
    prom = promedio(attribute)
    tolerancia = True

    operacion = desv/prom

    redondear = round(operacion,2)
    
    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":""}

    return resultado