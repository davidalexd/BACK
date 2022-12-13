from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion

def general_repetibilidad_cae(attribute):
    try:
        desv = desviacion_estandar_m(attribute)
        prom = promedio(attribute)
        tolerancia = True

        operacion = desv/prom

        redondear = round(operacion,2)
        
        if(redondear < 10):
            tolerancia = True
        else:
            tolerancia = False
        
        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":redondear,
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Ceificiente de variación <10",
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