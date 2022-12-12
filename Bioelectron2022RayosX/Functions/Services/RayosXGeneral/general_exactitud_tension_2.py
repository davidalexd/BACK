from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion

def general_exactitud_tension_2(element_1,attribute):
    try:
        prom = promedio(attribute)
        operacion = (prom-float(element_1[0]))/prom
        redondear = round(operacion*100,2)
        tolerancia=True
        
        if(redondear<10 or redondear<-10):
            tolerancia=True
        else:
            tolerancia=False

        estado = validacion([tolerancia])

        resultado =  {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"%",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"Desviaciones con respecto al valor nominal < ± 10% ",
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