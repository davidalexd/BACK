from Functions.Services.coeficiente_linealidad import coeficiente_linealidad
from Functions.Services.validacion import validacion
from Functions.Services.promedio import promedio

def mamografia_linealidad_rendimiento_carga_tubo(attribute=[0],attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute)):
        prom = promedio([attribute_1[x],attribute_2[x],attribute_3[x]])
        valor = float(attribute[x])/prom
        Uc.append(valor)
    
    coeLin = coeficiente_linealidad(Uc)
    
    redondear = round(coeLin,2)

    if(redondear<=0.1):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondear,
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"≤0.1",
        "estado":estado
        }
    

    return resultado