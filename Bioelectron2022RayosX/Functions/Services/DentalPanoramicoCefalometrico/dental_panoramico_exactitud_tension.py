from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def dental_panoramico_exactitud_tension(element,attribute):
    try:
        prom = promedio(attribute)
        element_1 = float(element[0])

        if(element_1 <= 0):
            operacion=0
        else:
            operacion = ((element_1-prom)/element_1)

        redondear = round(operacion*100,2)

        tolerancia_1 = 10
        tolerancia_2 = -10

        if (redondear < tolerancia_1 or redondear < tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"A "+str(element_1)+" kV",
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