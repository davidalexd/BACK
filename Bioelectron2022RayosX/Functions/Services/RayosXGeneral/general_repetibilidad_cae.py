from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_repetibilidad_cae(attribute):
    try:
        desv = desviacion_estandar_m(validacion_null_array(attribute))
        prom = promedio(validacion_null_array(attribute))
        tolerancia = True
        if(prom==0):
            operacion = 0
        else:
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