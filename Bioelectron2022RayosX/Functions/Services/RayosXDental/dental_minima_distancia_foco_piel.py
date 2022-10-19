def dental_minima_distancia_foco_piel(element):
    # llama Minima distancia
    resultado = [{"resultado":0}]
    operacion = float(element[0])
    redondear = round(operacion,2)

    tolerancia = True

    if (redondear >= 20):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"cm",
            "condicion":tolerancia
        }
    ]
    return resultado