from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_valor_rendimiento(element_1,attributes,element_2):
    try:
        prom = promedio(validacion_null_array(attributes))
        if(float(element_1[0])*float(element_2[0])**2 == 0 ):
               operacion = 0
        else:
            operacion = prom/float(element_1[0])*float(element_2[0])**2
        redondear = round(operacion,2)
        tolerancia=True

        if(redondear > 3 and redondear < 65):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" mGy/mAs",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"De modo orientativo, a 80 kV y con una filtración estimada entre 2.5 y 5 mmAl, el rendimiento estará entre 30 y 65 uGy/mAs a 1 m del foco",
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