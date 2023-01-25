from Functions.Services.promedio import promedio
from Functions.Services.DentalPanoramicoCefalometrico.dental_panoramico_valor_rendimiento import dental_panoramico_valor_rendimiento
from Functions.Services.validacion import validacion

def dental_panoramico_repetibilidad_rendimiento(element,element_1,element_2,attribute,attribute_2):
    try:
        dvr = dental_panoramico_valor_rendimiento(element,element_1,element_2,attribute)["data"][0]["resultado_salida"]
        prom = promedio(attribute_2)
        variante = float(element[0])*2

        if (dvr==0):
            operacion = 0
        else: 
            operacion = (prom*variante)/float(dvr)

        redondeo = round(operacion*100,2)

        tolerancia = True

        if(redondeo < 10):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"80 kV",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" %",
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