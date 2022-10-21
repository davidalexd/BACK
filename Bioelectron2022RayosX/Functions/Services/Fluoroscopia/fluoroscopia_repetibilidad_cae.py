from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_cae(attribute):
    resultado = [{"resultado":0}]
    desv = desviacion_estandar_m(attribute)
    prom = promedio(attribute)
    tolerancia = True

    if(prom == 0):
        operacion = 0
    else:
        operacion = desv/prom
    redondear = round(operacion,2)
    if(redondear<=10):
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
