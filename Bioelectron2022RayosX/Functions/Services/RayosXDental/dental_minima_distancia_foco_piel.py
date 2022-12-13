from Functions.Services.validacion import validacion

def dental_minima_distancia_foco_piel(element):
    try:
        # llama Minima distancia
        operacion = float(element[0])
        redondear = round(operacion,2)

        tolerancia = True

        if (redondear >= 20):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"cm",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"≥20 cm",
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