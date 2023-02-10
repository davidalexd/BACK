from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_variacion_rendimiento_carga(element_1,attributes,element_2,element_3):
    try:
        prom = promedio(validacion_null_array(attributes))
        variante_1 = prom/float(element_1[0])
        operacion = (variante_1-float(element_3[0])/float(element_2[0]))/(variante_1+float(element_3[0])/float(element_2[0]))
        redondear = round(operacion,2)
        tolerancia=True

        if(redondear<= 0.1):
            tolerancia=True
        else:
            tolerancia=False

        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear),
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Coeficiente de linealidad menor o igual que 0.1 entre pasos consecutivos ",
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