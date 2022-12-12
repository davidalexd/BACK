from Functions.Services.constantes_calculo_tolerancia_chr import constantes_calculo_tolerancia_chr
from Functions.Services.promedio import promedio
from Functions.Services.validacion import validacion


def mamografia_filtracion_capa_hemirreductora(element_1,element_2,attribute):
    try:
        tolerancia = True
        prom = promedio(attribute)
        redondear = round(prom,2)

        toleranci_1 = (float(element_2[0])/100)+0.03
        toleranci_2 = (float(element_2[0])/100)+ constantes_calculo_tolerancia_chr(element_1[0])

        if(redondear>=toleranci_1):
            tolerancia = True
        if(redondear<=toleranci_2):
            tolerancia = False
        else:
            tolerancia = None

        estado = validacion([tolerancia]) 

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" mmAl",
                    "estado":tolerancia
                }
            ],
            "tolerancia":toleranci_1+"≤CHR≤"+toleranci_2,
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