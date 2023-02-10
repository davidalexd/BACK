from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion
from Functions.Services.validacion_null_array import validacion_null_array

def general_exactitud_tiempo_exposicion_2(element_1,attribute):
    try:
        prom = promedio(validacion_null_array(attribute[0]))
        if(float(element_1[0])==0):
            operacion = 0
        else:  
            operacion = (prom-float(element_1[0]))/float(element_1[0])
        redondear = round(operacion*100,2)
        tolerancia=True

        if(redondear<10 or redondear<-10):
            tolerancia=True
        else:
            tolerancia=False
            
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
            "tolerancia":": Desviaciones con respecto al valor nominal < ± 10% para tiempos > 20 ms ",
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