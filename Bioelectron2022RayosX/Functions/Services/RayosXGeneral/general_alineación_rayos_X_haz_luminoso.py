from Functions.Services.suma_range import suma_range
from Functions.Services.validacion import validacion

def general_alineación_rayos_X_haz_luminoso(attribute,element):
    # attribute = Diferencia entre bordes (cm):
    # element = Distancia al Foco-Sistema de colimacion (cm):
    try:
        suma = suma_range(attribute)*(float(element[0])/100)
        tolerancia_1 = True
        tolerancia_2 = True

        redondear = round(suma,2)

        tolerancia_respuesta_1 = (3*float(element[0])/100)
        if(redondear<=tolerancia_respuesta_1):
            tolerancia_1 = True
        else:
            tolerancia_1 = False
        tolerancia_respuesta_2 = (2*float(element[0])/100)
        if(redondear<=tolerancia_respuesta_2):
            tolerancia_2 = True
        else:
            tolerancia_2 = False

        estado = validacion([tolerancia_1,tolerancia_2])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":redondear,
                    "estado":tolerancia_1
                },
                {
                    "parametros":"",
                    "resultado":redondear,
                    "estado":tolerancia_2
                }
            ],
            "tolerancia":"Suma de las desviaciones absolutas en los bordes inferiores al ± 2% de la distancia entre el foco y el maniquí de colimación para cada dirección principal. La suma total de las desviaciones absolutas no excederá, por otra parte, el 3% de la distancia entre el foco y maniquí de colimación.",
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