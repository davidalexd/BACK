
from Functions.Services.validacion import validacion
def tomograifa_exactitud_seleccion_posicion_corte_radiografia_planificacion(element):
    try:
        tolerancia =True
        redondear = round(float(element[0]),2)
        
        tolerancia_1 = 2
        tolerancia_2 = -2

        if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
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
                            "estado":tolerancia
                        }
                    ],
                    "tolerancia":"",
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