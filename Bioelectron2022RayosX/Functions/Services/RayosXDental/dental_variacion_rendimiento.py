
from Functions.Services.validacion import validacion
from Functions.Services.validacion_cero_negativo import validacion_cero_negativo

def dental_variacion_rendimiento(element_1,element_2,element_3,element_4,element_5,element_6):
    try:
        variacion_1 = float(element_4[0])*(float(element_2[0])**2)
        variacion_2 = float(element_3[0])*(float(element_1[0]))
        variacion_3 = float(element_6[0])*(float(element_2[0])**2)
        variacion_4 = float(element_5[0])*(float(element_1[0]))
        if(variacion_2==0):
            part_1 = 0
        else:
            part_1 = (variacion_1/variacion_2)
        if(variacion_4==0):
            part_2 = 0
        else:
            part_2 = (variacion_3/variacion_4)

        operacion_1 = part_1-part_2    
        operacion_2 = part_1+part_2
        
        if(operacion_2==0):
            operacion = 0
        else:
            operacion = operacion_1/operacion_2

        redondeo = round(operacion,2)
        tolerancia = True
        
        redondeo = validacion_cero_negativo(redondeo)

        if(redondeo <= 0.1):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"Coeficiente de linealidad "+str(redondeo),
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de linealidad ≤ 0.1 entre pasos consecutivos",
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