from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def dental_kerma_aire_entrada_paciente(attribute):
    try:
        prom = promedio(validacion_null_array(attribute))

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
    except Exception as e:
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"",
                    "estado":""
                }
            ],
            "tolerancia":"",
            "estado":"No Aplica"
            }
        return resultado