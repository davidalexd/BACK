def dental_tamano_campo_extremo_localizador(element):
    # llama Tamaño de Campo
    resultado = [{"resultado":0}]
    operacion = float(element[0])
    redondear = round(operacion,2)

    tolerancia = True

    if (redondear <= 6):
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