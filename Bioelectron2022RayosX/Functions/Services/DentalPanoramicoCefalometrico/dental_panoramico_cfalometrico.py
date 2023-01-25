from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_panoramico_cfalometrico(element,element_1,element_2,element_3):
    try:
        # LLAMA A TIEMPO S EN UN RANGO DE 5
        data = float(element[0])
        data_1= float(element_1[0])
        data_2 = float(element_2[0])
        data_3 = float(element_3[0])
        prom = promedio([data_1,data_2,data_3])
        if (data == 0):
            operacion = 0
        else:
            operacion = data-prom/data
            
        redondeo = round(operacion*100,2)
        tolerancia = True
        

        tolerancia_1 = 10
        tolerancia_2 = -10
        if (redondeo <= tolerancia_1 or redondeo <= tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"80 kV / Modo Cefalométrico",
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
