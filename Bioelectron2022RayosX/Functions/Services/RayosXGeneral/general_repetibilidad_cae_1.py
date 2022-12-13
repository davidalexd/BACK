from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto
from Functions.Services.validacion import validacion

def general_repetibilidad_cae_1(attribute,element):
    try:
        prom = promedio(attribute)
        tolerancia = True

        operacion = valor_absoluto((float(element[0])-prom)/float(element[0]))

        redondear = round(operacion*100,2)

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