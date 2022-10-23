from Functions.Services.promedio import promedio
def fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen(attribute_1=[0],attribute_2=[0],attribute_3=[0],attribute_4=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    tolerancia = True
    prom=promedio([attribute_2[0],attribute_3[0],attribute_4[0]])
    operacion = ((prom-float(attribute_1[0]))/prom)*100
    redondeo = round(operacion,2)

    tolerancia_1 = 20*float(attribute_1[0])/100
    tolerancia_2 = -20*float(attribute_1[0])/100

    if(redondeo<tolerancia_1 or redondeo<tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":redondeo,"condicion":tolerancia}],"tolerancia":"Variación < ±20% respecto de los valores de referencia"}


    return resultado