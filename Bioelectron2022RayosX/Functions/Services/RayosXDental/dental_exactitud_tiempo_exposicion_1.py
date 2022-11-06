from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
def dental_exactitud_tiempo_exposicion_1(element=[0],attribute=[0],opcion=[""]):
    # llama TIEMPO DE EXPOSICIÓN (s) y luego a tiempo en rango de 5
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    element_1 = float(element[0])
    prom = promedio(attribute)
    if element_1 == 0:
        operacion = 0
    else:
        operacion = (element_1-prom)/element_1

    redondeo = round(operacion*100,2)
    tolerancia = True

    if(opcion[0]=="EQUIPO MONOFÁSICO"):
        tolerancia_1 = 20
        tolerancia_2 = -20
        if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False
    else:
        tolerancia_1 = 10
        tolerancia_2 = -10
        if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "data":[
            {
                "condicion":"Tiempo "+str(element_1)+" s",
                "parametros":"",
                "resultado":"Desviación "+str(redondeo)+"%",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Desviación ≤± "+str(tolerancia_1)+"% ",
        "estado":estado
    }
    return resultado
