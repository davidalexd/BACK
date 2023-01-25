from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion
def dental_panoramico_panoramico_2(attribute):
    try:
        # llama TIEMPO DE EXPOSICIÓN (s) y luego a tiempo en rango de 5
        desv = desviacion_estandar_m(attribute)
        prom = promedio(attribute)

        if (prom==0):
            operacion = 0
        else:
            operacion = desv / prom

        redondeo=round(operacion,2)

        tolerancia = True
        
        if (redondeo < 10):
            tolerancia = True
        else:
            tolerancia = False
        
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"10 mAs / Modo Panorámico",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de variación < 10 % ",
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