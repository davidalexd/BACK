from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
def dental_panoramico_panoramico(element,attribute):
    try:
        # llama TIEMPO DE EXPOSICIÓN (s) y luego a tiempo en rango de 5
        element_1 = float(element[0])
        prom = promedio(attribute)

        if (element_1==0):
            operacion = 0
        else:
            operacion = (element_1 - prom) / element_1

        redondeo=round(operacion,2)

        tolerancia = True
        
        tolerancia_1 = 10
        tolerancia_2 = -10
        if (redondeo < tolerancia_1 or redondeo <tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False
        
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"80 kV / Modo Panorámico",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Desviaciones <± 10 % ",
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