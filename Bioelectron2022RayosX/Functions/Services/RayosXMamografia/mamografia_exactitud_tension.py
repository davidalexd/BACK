from Functions.Services.promedio import promedio
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def mamografia_exactitud_tension(attribute=[0],attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []
    for x in range(len(attribute)):
        prom = promedio([float(attribute_1[x]),float(attribute_2[x]),float(attribute_3[x])])
        operacion = float(attribute[x])-prom
        Uc.append(operacion)
    
    
    val_max = valor_maximo(Uc)
    abs = valor_absoluto(val_max)

    if(abs<=1 or abs<=-1):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":val_max+" kV",
                "estado":tolerancia
            },
        ],
        "tolerancia":"≤±1kV",
        "estado":estado
        }

    return  resultado