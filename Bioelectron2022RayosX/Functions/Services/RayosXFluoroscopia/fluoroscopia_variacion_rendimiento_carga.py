from Functions.Services.promedio import promedio

def fluoroscopia_variacion_rendimiento_carga(attributes_1=[0],attributes_2=[0],attributes_3=[0],element_1=[0],attributes_4=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    prom_1 = promedio([attributes_1[0],attributes_2[0],attributes_3[0]])
    prom_2 = promedio([attributes_1[1],attributes_2[1],attributes_3[1]])
    tolerancia = True
    cuad = float(element_1[0])**2
    part_1 = (((prom_1*cuad)/float(attributes_4[0]))-((prom_2*cuad)/float(attributes_4[1])))
    part_2 = (((prom_1*cuad)/float(attributes_4[0]))+((prom_2*cuad)/float(attributes_4[1])))
    

    if (part_2 == 0):
        operacion = 0
    else:
        operacion = part_1/part_2

    redondear = round(operacion,2)

    if(redondear<=0.1):
        tolerancia = True
    else:
        tolerancia = False

    
    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":"Coeficiente de linealidad   0.1"}

    return resultado