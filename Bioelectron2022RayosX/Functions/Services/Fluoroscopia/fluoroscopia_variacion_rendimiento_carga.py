from Functions.Services.promedio import promedio

def fluoroscopia_variacion_rendimiento_carga(attributes_1,attributes_2,element_1,element_2,element_3):
    resultado = [{"resultado":0}]

    prom_1 = promedio(attributes_1)
    prom_2 = promedio(attributes_2)
    cuad = float(element_1[0])**2
    part_1 = (((prom_1*cuad)/float(element_2[0]))-((prom_2*cuad)/float(element_3[0])))
    part_2 = (((prom_1*cuad)/float(element_2[0]))+((prom_2*cuad)/float(element_3[0])))

    if (part_2 == 0):
        operacion = 0
    else:
        operacion = part_1/part_2
        
    redondear = round(operacion,2)
    resultado = [{"resultado":redondear,"decorador":" "}]
    return resultado