def dental_exactitud_tiempo_exposicion_2(element_1=[0],element_2=[0]):
    # llama a TIEMPO DE EXPOSICIÓN (s) y luego a TIEMPO (s) in range 1
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    element_a = float(element_1[0])
    element_b = float(element_2[0])

    operacion = (element_a-element_b)/element_a

    redondeo = round(operacion,2)
    tolerancia = True
    tolerancia_1 = 10
    tolerancia_2 = -10

    if (redondeo <= tolerancia_1 or redondeo <=tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondeo)+"%","condicion":tolerancia}],"tolerancia":"Desviación menor o igual que ± 10%"}

    return resultado