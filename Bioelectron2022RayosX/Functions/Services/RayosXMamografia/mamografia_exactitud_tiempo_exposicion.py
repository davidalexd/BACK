from Functions.Services.validacion import validacion
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.valor_absoluto import valor_absoluto

def mamografia_exactitud_tiempo_exposicion(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],opcion=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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

    