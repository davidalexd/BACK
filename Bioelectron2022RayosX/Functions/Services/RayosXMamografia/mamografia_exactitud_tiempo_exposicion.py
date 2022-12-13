from Functions.Services.validacion import validacion
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.valor_absoluto import valor_absoluto

def mamografia_exactitud_tiempo_exposicion(attribute_1,attribute_2,attribute_3,attribute_4,opcion):
    try:
        tolerancia = True
        Uc = []
        for x in range(len(attribute_1)):
            desv = desviacion_estandar_m([attribute_1[x],attribute_2[x],attribute_3[x],attribute_4[x]])
            Uc.append(desv)
        
        max = valor_maximo(Uc)

        abs = valor_absoluto(max)

        redondear = round(max,2)

        if(float(opcion[0])>=200):
            tolerancia_valor = 10
        else:
            tolerancia_valor = 15


        if (abs<tolerancia_valor):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia]) 

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"<±"+tolerancia_valor+"%",
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

    