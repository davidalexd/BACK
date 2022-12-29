from Functions.Services.promedio import promedio
from Functions.Services.valor_maximo import valor_maximo 
from Functions.Services.valor_minimo import valor_minimo 
from Functions.Services.validacion import validacion

def tomografia_variacion_rendimiento_carga(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0],attribute_5=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []

    for x in range(len(attribute_1)):
        prom = promedio([attribute_2[x],attribute_3[x],attribute_4[x]])
        correcion = prom - attribute_5[x]

        if(attribute_1[x]==0):
            operacion = 0
        else:
            operacion = correcion/attribute_1[x]
        
        Uc.append(operacion)
    
    
    operacion_2 = (valor_maximo(Uc)-valor_minimo(Uc))/(Uc[0]+Uc[1])

    redondear = round(operacion_2,2)
    
    if(redondear <= 0.1):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia]) 

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+"%",
                "estado":tolerancia
            }
        ],
        "tolerancia":"≤ 0.1 (Coeficiente de Linealidad).",
        "estado":estado
        }

    
    return resultado