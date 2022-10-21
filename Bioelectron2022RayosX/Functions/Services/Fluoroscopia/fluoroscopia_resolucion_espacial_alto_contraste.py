def fluoroscopia_resolucion_espacial_alto_contraste(attribute):
    ordenador = [0,1,2,3]
    tolerancia = True
    tolerancias = [0.9,1.12,1.2,1.6]
    Uc = []

    for x in ordenador:
        operacion = float(attribute[x])
        redondear = round(operacion,2)

        if(redondear >= tolerancias[x]):
            tolerancia = True
        else:
            tolerancia = False

        Uc.append({
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        })
    
    resultado = Uc
    
    return resultado