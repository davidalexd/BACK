from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio

def dental_repetibilidad_tension(attribute):
    # llama a TENSION PROMEDIO (kV)
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
