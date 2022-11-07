from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_kerma_aire_entrada_paciente(attribute_1=[0],attribute_2=[0],attribute_3=[0],element=[0],opcion=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    prom=promedio([attribute_1[0],attribute_2[0],attribute_3[0]])
    operacion = prom*float(element[0])**2
    redondeo= round(operacion,2)

    if(redondeo<float(opcion[0])):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "exploracion":"Torax PA",
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondeo+"mGy",
                "estado":tolerancia
            }
        ],
        "tolerancia":"<"+opcion[0]+"mGy",
        "estado":estado
        }

    return resultado