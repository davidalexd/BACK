from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def dental_repetibilidad_tiempo_exposicion(element,attribute):
    try:
        # LLAMA A TIEMPO S EN UN RANGO DE 5
        desvm = desviacion_estandar_m(validacion_null_array(attribute))
        prom = promedio(validacion_null_array(attribute))
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
            "condicion":"Tiempo "+str(element_1)+" s",
            "data":[
                {
                    "parametros":"",
                    "resultado":"Coeficiente de variación "+str(redondear)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de variación ≤ 10% ",
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
