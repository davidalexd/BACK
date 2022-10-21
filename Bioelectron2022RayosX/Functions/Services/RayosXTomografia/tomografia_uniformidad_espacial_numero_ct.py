from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 

def tomografia_uniformidad_espacial_numero_ct(element, attribute):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    Uc = []
    tolerancia = True

    for x in attribute:
        operacion = float(element[0])-float(x)
        Uc.append(operacion)
        
    if(valor_absoluto(valor_maximo(Uc))>=valor_absoluto(valor_minimo(Uc))):
        operacion_2 = valor_maximo(Uc)
    else:
        operacion_2 = valor_minimo(Uc)
        
    redondear = round(operacion_2,2)

    if(redondear <= 5):
        tolerancia = True
    else:
        tolerancia = False
        
    return resultado = [{"parametros":"","resultado":redondear,"condicion":tolerancia}]
    



