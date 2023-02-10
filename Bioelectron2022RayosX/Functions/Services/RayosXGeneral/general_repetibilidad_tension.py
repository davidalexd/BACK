from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_repetibilidad_tension(attributes):
    try:
        prom = promedio(validacion_null_array(attributes))
        desv = desviacion_estandar_m(validacion_null_array(attributes))

        if(prom==0):
            operacion = 0
        else:
            operacion =(desv/prom)*100

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