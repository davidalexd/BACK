from Functions.Services.coeficiente_variacion import coeficiente_variacion
from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.validacion import validacion

def mamografia_repetibilidad_tiempo_exposicion(attributes_1=[0],attributes_2=[0],attributes_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    Uc = []
    
    for x in range(len(attributes_1)):
        cf_var = coeficiente_variacion([attributes_1[x],attributes_2[x],attributes_3[x]])
        Uc.append(cf_var)
    
    max = valor_maximo(Uc)

    redondear = round(max,2)

    if(max < 10):
        tolerancia = True
    else:
        tolerancia = False
    
    estado = validacion([tolerancia]) 

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+" %",
                "estado":tolerancia
            }
        ],
        "tolerancia":"<10%",
        "estado":estado
        }

    return resultado