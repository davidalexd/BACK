from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion
def dental_panoramico_cfalometrico_2(element,element_1,element_2):
    try:
        data_1= float(element[0])
        data_2 = float(element_1[0])
        data_3 = float(element_2[0])
        # llama TIEMPO DE EXPOSICIÓN (s) y luego a tiempo en rango de 5
        desv = desviacion_estandar_m([data_1,data_2,data_3])
        prom = promedio([data_1,data_2,data_3])

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
            "condicion":"10 mAs / Modo Cefalométrico",
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