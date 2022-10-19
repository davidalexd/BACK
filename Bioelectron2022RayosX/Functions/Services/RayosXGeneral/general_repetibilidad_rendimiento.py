from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def general_repetibilidad_rendimiento(attribute):
    resultado = [{"resultado":0}]
    desv = desviacion_estandar_m(attribute)
    prom = promedio(attribute)
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