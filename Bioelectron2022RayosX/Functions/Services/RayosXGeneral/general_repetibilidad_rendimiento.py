from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion

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