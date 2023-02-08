from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def mamografia_uniformidad_imagen(attribute_1,attribute_3):
    try:
        tolerancia_1 = True
        tolerancia_2 = True

        maxDesbPrc_1 = maxima_desviacion_absoluta_procentual(attribute_1)
        maxDesbPrc_2 = maxima_desviacion_absoluta_procentual(attribute_3)

        if(valor_absoluto(maxDesbPrc_1)<=15 or valor_absoluto(maxDesbPrc_1)<=-15 ):
            tolerancia_1 = True
        else:
            tolerancia_1 = False

        if(valor_absoluto(maxDesbPrc_2)<=20 or valor_absoluto(maxDesbPrc_2)<=-20 ):
            tolerancia_2 = True
        else:
            tolerancia_2 = False

                
        estado = validacion([tolerancia_1,tolerancia_2])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"VMP = "+maxDesbPrc_1+" %",
                    "estado":tolerancia_1
                },
                {
                    "parametros":"",
                    "resultado":"RSR = "+maxDesbPrc_2+" %",
                    "estado":tolerancia_2
                },
            ]
            ,"tolerancia":"Desviación máxima VMP ≤ ±15%, Desviación máxima RSR ≤ ±20%.",
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