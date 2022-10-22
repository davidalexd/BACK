def tomografia_perfiles_sensibilidad(attribute_1=[0],attribute_2=[0]):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    tolerancia = True
    tolerancia_1 = 1
    tolerancia_2 = -1
    Uc = []
    
    for x in range(len(attribute_1)):
        operacion = float(attribute_1[x])-float(attribute_2[x])
        redondear = round(operacion,2)


        if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
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