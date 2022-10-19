def fluoroscopia_tamano_campo_entrada_detector_imagen(attributes_1,attributes_2):
    resultado = [{"resultado":0}]
    Uc = []
    for x in range(len(attributes_1)):
        if (float(attributes_1[x])==0.0):
            valor_resultante = 0
        else:
            valor_resultante = float(attributes_2[x])/float(attributes_1[x])

        redondear = round(valor_resultante,2)
        
        Uc.append({"resultado":redondear,"decorador":" "})
        
    resultado = Uc
    return resultado