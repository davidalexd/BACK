from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.validacion import validacion

def fluoroscopia_repetibilidad_tension(attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    prom = promedio([attribute_1[1],attribute_2[1],attribute_3[1]])
    des_v = desviacion_estandar_m([attribute_1[1],attribute_2[1],attribute_3[1]])
    if (prom == 0):
        operacion = 0
    else:
        operacion = des_v/prom   

    redondear = round(operacion,2)

    if(redondear < 5):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondear+" %",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Coeficiente de variación < 5%",
        "estado":estado
        }

    return resultado