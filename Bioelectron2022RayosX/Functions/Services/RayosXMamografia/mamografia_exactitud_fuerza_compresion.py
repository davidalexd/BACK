from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.validacion import validacion

def mamografia_exactitud_fuerza_compresion(attribute_1=[0],attribute_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    Uc = []

    for x in range(len(attribute_1)):
        operacion = attribute_1[x]-attribute_2[x]
        Uc.append(operacion)
    
    max = valor_maximo(Uc)

    if(max<=20 or max<=-20):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":max+"N",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"≤±20N",
        "estado":estado
        }
        
    return resultado 
    

    
