
from Functions.Services.validacion import validacion
from Functions.Services.promedio import promedio

def dental_filtracion(element,attribute):
    try:
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
            "condicion":"Tensión "+str(element_1)+" kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":"Filtración total "+str(redondeo)+" mm Al",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Filtración total ≥ 1.5 mm Al ",
            "estado":estado
            }

        return resultado
    except Exception as e:
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"",
                    "estado":""
                }
            ],
            "tolerancia":"",
            "estado":"No Aplica"
            }
        return resultado