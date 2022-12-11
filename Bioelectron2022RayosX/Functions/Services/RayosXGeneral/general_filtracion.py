from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def general_filtracion(attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    redondear = round(prom,2)
    tolerancia=True

    if(redondear > 2.5):
        tolerancia=True
    else:
        tolerancia=False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+"mmAl",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Filtración > 2.5 mm equivalentes de aluminio",
        "estado":estado
        }

    return resultado