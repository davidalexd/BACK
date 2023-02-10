from Functions.Services.validacion import validacion

def general_exactitud_tiempo_exposicion_1(element_1,element_2):
    try:
        if(float(element_1[0])==0):
               operacion = 0
        else:
               operacion = (float(element_2[0])-float(element_1[0]))/float(element_1[0])*100

        redondear = round(operacion,2)
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
            "tolerancia":"Desviaciones con respecto al valor nominal < ± 10% para tiempos > 20 ms ",
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