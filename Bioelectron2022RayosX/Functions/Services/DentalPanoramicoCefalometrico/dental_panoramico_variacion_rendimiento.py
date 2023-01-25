
from Functions.Services.validacion import validacion
from Functions.Services.promedio import promedio

def dental_panoramico_variacion_rendimiento(element,element_1,element_2,attribute,element_3,element_4,attribute_2):
    try:
        prom_1 = promedio(attribute)
        prom_2 = promedio(attribute_2)
        variante = float(element[0])**2
        variante_1 = float(element_1[0])
        variante_2 = float(element_2[0])
        variante_3 = float(element_3[0])
        variante_4 = float(element_4[0])
        
        operacion_1 = ((prom_1*variante)/(variante_1*variante_2))-((prom_2*variante)/(variante_3*variante_4))
        operacion_2 = ((prom_1*variante)/(variante_1*variante_2))+((prom_2*variante))

        if (operacion_2 == 0):
            operacion = 0 
        else:
            operacion = operacion_1/operacion_2

        redondeo = round(operacion,2)
        tolerancia = True

        if(redondeo <= 0.1):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":str(variante_1)+" kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo),
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de linealidad ≤ 0.1",
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