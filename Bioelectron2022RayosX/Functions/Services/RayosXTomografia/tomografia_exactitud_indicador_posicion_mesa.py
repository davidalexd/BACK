from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def tomografia_exactitud_indicador_posicion_mesa(element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia =True
    abs = valor_absoluto(float(element_3[0])-float(element_1[0]))
    operacion = float(element_2[0])-abs

    redondear = round(operacion,2)
    
    if(redondear <= 2):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+" mm",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Desviación ≤ ±2 mm",
        "estado":estado
        }

    return resultado