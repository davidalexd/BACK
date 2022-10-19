from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio


def general_repetibilidad_tension(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    desv = desviacion_estandar_m(attributes)
    operacion = desv/prom
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado