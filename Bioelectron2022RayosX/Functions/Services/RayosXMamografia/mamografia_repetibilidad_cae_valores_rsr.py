from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.validacion import validacion

def mamografia_repetibilidad_cae_valores_rsr(attribute_1=[0],attribute_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute_1)):
        Uc.append(float(attribute_1[x])/float(attribute_2[x]))

    maxDesvPrc = maxima_desviacion_absoluta_procentual(Uc)
    redondear = round(maxDesvPrc,2)

    if(valor_absoluto(devAbsPrc)<=5 or valor_absoluto(devAbsPrc)<=-5):
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
            },
        ]
        ,"tolerancia":"≤±5%",
        "estado":estado
        }
    

    return resultado