from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion


def general_repetibilidad_tiempo_exposicion(attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    desv = desviacion_estandar_m(attributes)
    operacion = desv/prom
    redondear = round(operacion*100,2)
    tolerancia=True
    
    estado = validacion([tolerancia])
    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+"%",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Coeficiente de variación < 10% ",
        "estado":estado
        }

    return resultado