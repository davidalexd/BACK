from Functions.Services.maxima_desviacion_absoluta_procentual import maxima_desviacion_absoluta_procentual
from Functions.Services.maxima_desviacion_absoluta import maxima_desviacion_absoluta
from Functions.Services.validacion import validacion

def mamografia_repetibilidad_rendimiento(attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute_1)):
        devPrc = maxima_desviacion_absoluta_procentual([attribute_1[x],attribute_2[x],attribute_3[x]])
        Uc.append(devPrc)
    
    maxDesvAbs = maxima_desviacion_absoluta(Uc)

    redondear = round(maxDesvAbs,2)

    if(redondear<=5):
        tolerancia = True
    else:
        tolerancia= False

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
        "tolerancia":"≤5%",
        "estado":estado
        }

    return resultado