from Functions.Services.validacion import validacion

def dental_minima_distancia_foco_piel(element=[0]):
    # llama Minima distancia
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = float(element[0])
    redondear = round(operacion,2)

    tolerancia = True

    if (redondear >= 20):
        tolerancia = True
    else:
        tolerancia = False

    estado = validacion([tolerancia])

    resultado = {
        "data":[
            {
                "condicion":"",
                "parametros":"",
                "resultado":str(redondear)+"cm",
                "estado":tolerancia
            }
        ],
        "tolerancia":"≥20 cm",
        "estado":estado
        }

    return resultado