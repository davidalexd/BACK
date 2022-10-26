from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio

def dental_repetibilidad_tiempo_exposicion(attribute=[0]):
# LLAMA A TIEMPO S EN UN RANGO DE 5
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    desvm = desviacion_estandar_m(attribute)
    prom = promedio(attribute)

    operacion = desvm/prom
    redondear = round(operacion*100,2)
    tolerancia = True
    

    if(redondear < 10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación menor o igual que 10% "}

    return resultado
