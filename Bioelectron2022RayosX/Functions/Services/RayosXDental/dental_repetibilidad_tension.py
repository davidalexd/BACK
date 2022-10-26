from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio

def dental_repetibilidad_tension(attribute=[0]):
    # llama a TENSION PROMEDIO (kV)
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

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación < 10% "}

    return resultado
