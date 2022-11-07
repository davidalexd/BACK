from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_exactitud_tension(element=[0],attribute=[0]):
    # llama TENSION NOMINAL  (kV) luego a TENSION PROMEDIO (kV) range (5)
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    element_1 = float(element[0])

    if(element_1 <= 0):
        operacion=0*100
    else:
        operacion = ((element_1-prom)/element_1)*100
    redondear = round(operacion,2)

    tolerancia_1 = 10
    tolerancia_2 = -10

    if (redondear < tolerancia_1 or redondear < tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"Tensión "+str(element_1)+" kV",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondear)+"%",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Desviación <±10%",
        "estado":estado
        }
    
    return resultado