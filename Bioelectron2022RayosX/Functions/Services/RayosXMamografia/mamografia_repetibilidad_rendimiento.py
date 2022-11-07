from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.validacion import validacion

def mamografia_repetibilidad_rendimiento(attribute=[0],attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute)):
        prom = promedio([attribute_1[x],attribute_2[x],attribute_3[x]])
        valor = float(attribute[x])/prom
        Uc.append(valor)
    
    max = valor_maximo(Uc)

    redondear = round(max,2)
   
    estado = validacion([tolerancia]) 

    
    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+" µGy/mAs",
                "estado":tolerancia
            }
        ],
        "tolerancia":"",
        "estado":estado
        }

    return resultado