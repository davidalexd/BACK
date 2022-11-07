from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.validacion import validacion

def mamografia_uniformidad_imagen(attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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

            
    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":maxDesbPrc_1+" %",
                "estado":tolerancia
            },
            {
                "parametros":"",
                "resultado":maxDesbPrc_2+" %",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"",
        "estado":estado
        }
    

    return resultado