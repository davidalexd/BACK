def fluoroscopia_resolucion_espacial_alto_contraste(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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
    
    resultado = {"data":Uc,"tolerancia":"Tamaño de campo de 36 cm ≥ 0,9-1 pl/mm; de 30 cm ≥ 1,12 pl/mm; de 23 cm ≥ 1,2 pl/mm; de 15 cm o inferiores ≥ 1,6 pl/mm"}
    
    return resultado