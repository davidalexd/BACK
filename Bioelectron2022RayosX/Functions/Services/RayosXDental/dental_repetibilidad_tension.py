from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_repetibilidad_tension(element,attribute=[0]):
    # llama a TENSION PROMEDIO (kV)
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    desvm = desviacion_estandar_m(attribute)
    prom = promedio(attribute)
    element_1 = float(element[0])

    operacion = desvm/prom
    redondear = round(operacion*100,2)
    tolerancia = True
    

    if(redondear < 10):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"Tensión "+str(element_1)+" kV",
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
