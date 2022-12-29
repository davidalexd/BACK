from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion


def tomografia_ruido_imagen(attributes_1=[0],attributes_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia_1 =True
    tolerancia_2 =True

    desv_1 = desviacion_estandar_m(attributes_1)
    desv_2 = desviacion_estandar_m(attributes_2)

    redondear_1 = round(desv_1,2)
    redondear_2 = round(desv_2,2)

    if(redondear_1<=5):
        tolerancia_1 = True
    else:
        tolerancia_1 = False
    
    if(redondear_2<=20):
        tolerancia_2 = True
    else:
        tolerancia_2 = False

    estado = validacion([tolerancia_1,tolerancia_2])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear_1)+"UH",
                "estado":tolerancia_1
            },
            {
                "parametros":"",
                "resultado":str(redondear_2)+"UH",
                "estado":tolerancia_2
            }
        ],
        "tolerancia":"La desviación típica para las exploraciones de cerebro adulto sea ≤ 5 UH o ≤ 20 UH para las de abdomen y tórax de rutina adulto.",
        "estado":estado
        }

    return resultado


