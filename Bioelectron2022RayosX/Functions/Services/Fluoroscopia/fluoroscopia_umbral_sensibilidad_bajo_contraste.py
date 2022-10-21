def fluoroscopia_umbral_sensibilidad_bajo_contraste(attribute_1,attribute_2):
    ordenador = [0,1,2,3]
    tolerancia = True
    tolerancias = [4,3.5,2.7,1.9]
    Uc = []

    for x in ordenador:
        operacion = float(attribute_1[x])/float(attribute_2[x])
        redondear = round(operacion,2)

        
        if(redondear <= tolerancias[x]):
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
    
