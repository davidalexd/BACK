from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_repetibilidad_cae_1(attribute,element):
    try:
        prom = promedio(validacion_null_array(attribute))
        tolerancia = True

        operacion = valor_absoluto((float(element[0])-prom)/float(element[0]))
        # operacion = (float(element[0])-prom)/float(element[0])

        redondear = round(operacion,2)
        # redondear = round(operacion,2)

        if(redondear <= 20 or redondear <=-20):
            tolerancia = True
        else:
            tolerancia = False
        
        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"%",
                    "condicion":tolerancia
                } 
            ],
            "tolerancia":"≤± 20",
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