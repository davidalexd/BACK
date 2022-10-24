def general_exactitud_tiempo_exposicion_1(element_1=[0],element_2=[0]):
    # element_1 = TIEMPO #1 
    # element_2 = TIEMPO range 1

    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = (element_2[0]-element_1[0])/element_1[0]
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Desviaciones con respecto al valor nominal < ± 10% para tiempos > 20 ms "}

    return resultado