from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio

def dental_repetibilidad_tiempo_exposicion(attribute):
# LLAMA A TIEMPO S EN UN RANGO DE 5
    resultado =  [{"resultado":0}]
    desvm = desviacion_estandar_m(attribute)
    prom = promedio(attribute)

    operacion = desvm/prom
    redondear = round(operacion,2)
    tolerancia = True
    

    if(redondear < 10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado
