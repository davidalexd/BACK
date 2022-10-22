from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 

def tomografia_exactitud_tension(attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    ordenador = [0,1,2]
    tolerancia = True
    Uc = []

    for x in ordenador:
        prom = promedio(attribute_2[x])
        correcion = prom-float(attribute_3[x])
        operacion = (float(attribute_1[x])-correcion)*100/correcion

        redondear = round(operacion,2)
        
        Uc.append(redondear)
    
    if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
        operacion_2 = valor_maximo(Uc)
    else:
        operacion_2 = valor_minimo(Uc)

    redondear = round(operacion_2,2)
    tolerancia_1 = 5
    tolerancia_2 = -5

    if(operacion_2 <= tolerancia_1 or operacion_2 <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
        {
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        }
    ]

    return resultado

