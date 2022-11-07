from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_kerma_aire_entrada_paciente(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)

    operacion = (prom/1000)*1.1

    redondeo=round(operacion,2)

    tolerancia = True

    if (redondeo < 4):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "condicion":"Exploración molar superior adulto ",
        "data":[
            {
                "parametros":"",
                "resultado":str(redondeo)+" mGy",
                "estado":tolerancia
            }
        ],
        "tolerancia":"Deberá ser inferior a 4 mGy",
        "estado":estado
        }

    return resultado