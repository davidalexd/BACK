from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_kerma_aire_entrada_paciente(attribute_1,attribute_2,attribute_3,element,opcion):
    try:
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
                    "resultado":str(redondeo)+"mGy",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"<"+str(opcion[0])+"mGy",
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