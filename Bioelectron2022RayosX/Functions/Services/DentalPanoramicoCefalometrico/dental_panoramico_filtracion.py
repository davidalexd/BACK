
from Functions.Services.validacion import validacion
from Functions.Services.promedio import promedio

def dental_panoramico_filtracion(element,attribute):
    try:
        prom = promedio(attribute)
        element_1 = float(element[0])
        redondeo=round(prom,2)

        tolerancia = True
        if (element_1 <= 70 ):
            if (redondeo >= 1.5):
                tolerancia = True
            else:
                tolerancia = False
        else:
            if (redondeo >= 2.5):
                tolerancia = True
            else:
                tolerancia = False


        estado = validacion([tolerancia])

        resultado = {
            "condicion":"Tensión "+str(element_1)+" kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" mm equivalentes de aluminio para "+str(element_1)+" kV",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Filtración Total > 1.5 mm aluminio para tensiones ≤ 70 kVp. Filtración Total ≥ 2.5 mm aluminio para tensiones > 70 kVp.",
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