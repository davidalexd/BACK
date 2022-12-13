from Functions.Services.maxima_desviacion_absoluta import maxima_desviacion_absoluta
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.validacion import validacion

def mamografia_repetibilidad_tension(attributes_1,attributes_2,attributes_3):
    try:
        tolerancia = True
        max_desv_abs_1 = maxima_desviacion_absoluta(attributes_1)
        max_desv_abs_2 = maxima_desviacion_absoluta(attributes_2)
        max_desv_abs_3 = maxima_desviacion_absoluta(attributes_3)

        operacion = valor_maximo([max_desv_abs_1,max_desv_abs_2,max_desv_abs_3])
        
        redondear = round(operacion,2)

        if valor_absoluto(redondear)<=0.5 or valor_absoluto(redondear)<= -0.5:
            tolerancia = True
        else:
            tolerancia = False
            
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" kV",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"≤±0.5kV",
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
