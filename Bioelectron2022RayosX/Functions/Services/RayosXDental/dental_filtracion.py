
from Functions.Services.validacion import validacion
from Functions.Services.promedio import promedio

def dental_filtracion(element,attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    redondeo=round(prom,2)
    element_1 = float(element[0])

    tolerancia = True
    if (redondeo >= 1.5):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "data":[
            {
                "condicion":"Tensión "+str(element_1)+" kV",
                "parametros":"",
                "resultado":"Filtración total "+str(redondeo)+" mm Al",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Filtración total ≥ 1.5 mm Al ",
        "estado":estado
        }

    return resultado
