from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def general_repetibilidad_tension(attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    desv = desviacion_estandar_m(attributes)
    operacion = (desv/prom)*100
    redondear = round(operacion,2)
    tolerancia=True
    
    if(redondear<5):
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
        "tolerancia":"Coeficiente de variación < 5%. ",
        "estado":estado
        }

    return resultado