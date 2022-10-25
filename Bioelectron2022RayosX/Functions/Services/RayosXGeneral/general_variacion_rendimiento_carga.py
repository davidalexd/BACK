from Functions.Services.promedio import promedio

def general_variacion_rendimiento_carga(element_1=[0],attributes=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    variante_1 = prom/float(element_1[0])
    operacion = (variante_1-float(element_3[0])/float(element_2[0]))/(variante_1+float(element_3[0])/float(element_2[0]))
    redondear = round(operacion,2)
    tolerancia=True

    if(redondear<= 0.1):
        tolerancia=True
    else:
        tolerancia=False

    
    resultado = {"data":[{"parametros":"","resultado":str(redondear),"condicion":tolerancia}],"tolerancia":"Coeficiente de linealidad menor o igual que 0.1 entre pasos consecutivos "}

    return resultado