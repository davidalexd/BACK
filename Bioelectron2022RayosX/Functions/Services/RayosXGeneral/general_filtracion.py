from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_filtracion(attributes):
    try:
        prom = promedio(validacion_null_array(attributes))
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
                    "resultado":str(redondear)+" mmAl",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Filtración > 2.5 mm equivalentes de aluminio",
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