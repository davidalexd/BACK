from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def mamografia_fuerza_compresion_atenuacion_compresor(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia_1 = True
    tolerancia_2 = True

    if(valor_absoluto(element_1[0])<=300):
        tolerancia_1 = True
    else:
        tolerancia_1 = False

    if(element_2[0]>150 and element_2[0]<200):
        tolerancia_2 = True
    else:
        tolerancia_2 = False
    
    
    estado = validacion([tolerancia_1,tolerancia_2])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":element_1[0]+"N",
                "estado":tolerancia_1
            },
            {
                "parametros":"",
                "resultado":element_2[0]+"N",
                "estado":tolerancia_2
            }
        ]
        ,"tolerancia":"",
        "estado":estado
        }
    return resultado
    