from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_valor_rendimiento(element=[0],attribute=[0],element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    variante = float(element[0])
    variante_1 = float(element_3[0])**2
    variante_2 = float(element_2[0])*float(element_1[0])
    operacion = (prom*variante_1)/variante_2
    redondeo = round(operacion,2)
    tolerancia = True

    if(redondeo > 25):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"Tensión "+str(variante)+" kV",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondeo)+" uGy/mAs a 1 m del foco",
                "resultado_salida":redondeo,
                "estado":tolerancia
            }
        ],
        "tolerancia":"Superior a 25 uGy/mAs a 1 m del foco y a la tensión de disparo",
        "estado":estado
        }

    return resultado