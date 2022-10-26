from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def general_repetibilidad_rendimiento(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    desv = desviacion_estandar_m(attribute)
    prom = promedio(attribute)
    operacion = desv/prom
    redondear = round(operacion*100,2)
    tolerancia=True

    if(redondear<10):
        tolerancia=True
    else:
        tolerancia=False
    
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación < 10% "}

    return resultado