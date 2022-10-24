def dental_tamano_campo_extremo_localizador(element=[0]):
    # llama Tamaño de Campo
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = float(element[0])
    redondear = round(operacion,2)

    tolerancia = True

    if (redondear <= 6):
        tolerancia = True
    else:
        tolerancia = False
        
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"cm","condicion":tolerancia}],"tolerancia":"Menor o igual que 6 cm "}
    
    return resultado