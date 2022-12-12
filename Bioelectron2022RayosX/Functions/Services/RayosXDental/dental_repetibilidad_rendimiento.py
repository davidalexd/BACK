from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.RayosXDental.dental_valor_rendimiento import dental_valor_rendimiento
from Functions.Services.validacion import validacion

def dental_repetibilidad_rendimiento(element,attribute,element_1,element_2,element_3):
    try:
        dvr = dental_valor_rendimiento(element,attribute,element_1,element_2,element_3)["data"][0]["resultado_salida"]
        desvm = desviacion_estandar_m(attribute)
        variante_1 = float(element_1[0])*2
        variante = float(element[0])
        operacion = (desvm*variante_1)/float(dvr)

        redondeo = round(operacion*100,2)

        tolerancia = True

        if(redondeo < 10):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"Tensión "+str(variante)+" kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":"Coeficiente de variación "+str(redondeo)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de variación < 10% ",
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