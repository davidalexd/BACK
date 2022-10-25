from Functions.Services.promedio import promedio


def general_exactitud_tiempo_exposicion_2(element_1=[0],attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    operacion = (prom-float(element_1[0]))/float(element_1[0])
    redondear = round(operacion,2)
    tolerancia=True

    if(redondear<10 or redondear<-10):
        tolerancia=True
    else:
        tolerancia=False
        
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":": Desviaciones con respecto al valor nominal < ± 10% para tiempos > 20 ms "}

    return resultado