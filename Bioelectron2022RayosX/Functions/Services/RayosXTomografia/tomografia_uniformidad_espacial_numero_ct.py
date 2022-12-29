from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 
from Functions.Services.validacion import validacion

def tomografia_uniformidad_espacial_numero_ct(element=[0], attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in attribute:
        operacion = float(element[0])-float(x)
        Uc.append(operacion)
        
    if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
        operacion_2 = valor_maximo(Uc)
    else:
        operacion_2 = valor_minimo(Uc)
        
    redondear = round(operacion_2,2)

    if(valor_absoluto(redondear) < 5 or valor_absoluto(redondear) < -5):
        tolerancia = True
    else:
        tolerancia = False
        
    estado = validacion([tolerancia])
    
    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondear + " UH",
                "estado":tolerancia
            }
        ],
        "tolerancia":"< ±5 UH.",
        "estado":estado
        }
    
    return resultado
    



