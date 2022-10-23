from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 

def tomografia_exactitud_tension(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],attribute_5=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    ordenador = [0,1,2]
    tolerancia = True
    Uc = []

    for x in range(len(attribute_1)):
        prom = promedio([attribute_2[x],attribute_3[x],attribute_4[x]])
        correcion = prom-float(attribute_5[x])
        operacion = (float(attribute_1[x])-correcion)*100/float(attribute_1[x])

        redondear = round(operacion,2)
        
        Uc.append(redondear)
    
    if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
        operacion_2 = valor_maximo(Uc)
    else:
        operacion_2 = valor_minimo(Uc)

    redondear_2 = round(valor_absoluto(operacion_2),2)
    tolerancia_1 = 5
    tolerancia_2 = -5

    if(redondear_2 <= tolerancia_1 or redondear_2 <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":redondear_2,"condicion":tolerancia}],"tolerancia":"Desviación ≤ ±5% (entre 80 y 140 kVp)."}

    return resultado

