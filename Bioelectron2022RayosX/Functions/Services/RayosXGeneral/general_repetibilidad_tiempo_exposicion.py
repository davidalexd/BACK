from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio


def general_repetibilidad_tiempo_exposicion(attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    desv = desviacion_estandar_m(attributes)
    operacion = desv/prom
    redondear = round(operacion*100,2)
    tolerancia=True
    
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación < 10% "}

    return resultado