from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 
from Functions.Services.validacion import validacion

def tomografia_repetibilidad_rendimiento(attribute_1,attribute_2,attribute_3):
    try:
        tolerancia = True
        Uc = []

        for x in range(len(attribute_1)):
            desv = desviacion_estandar_m([attribute_1[x],attribute_2[x],attribute_3[x]])
            prom = promedio([attribute_1[x],attribute_2[x],attribute_3[x]])

            if(prom == 0):
                operacion = 0
            else:
                operacion = desv*100/prom
                
            redondear = round(operacion,2)
            
            Uc.append(operacion)
        
        
        if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
            operacion_2 = valor_maximo(Uc)
        else:
            operacion_2 = valor_minimo(Uc)
        
        redondear = round(operacion_2,2)

        if(redondear <= 5):
            tolerancia = True
        else:
            tolerancia = False
        
        estado = validacion([tolerancia]) 

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":redondear+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"< ±5%. ",
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
