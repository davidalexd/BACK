from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen(attribute_1,attribute_2,attribute_3,attribute_4):
    try:
        tolerancia = True
        prom=promedio([attribute_2[0],attribute_3[0],attribute_4[0]])
        operacion = ((prom-float(attribute_1[0]))/float(attribute_1[0]))*100
        redondeo = round(operacion,2)

        tolerancia_1 = 20*float(attribute_1[0])/100
        tolerancia_2 = -20*float(attribute_1[0])/100

        if(redondeo<tolerancia_1 or redondeo<tolerancia_2):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])
        
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondeo)+" %",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Variación < ±20% respecto de los valores de referencia",
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