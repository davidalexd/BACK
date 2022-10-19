from Functions.Services.promedio import promedio

def fluoroscopia_valor_rendimiento(attribute,element_1,element_2):
    resultado = [{"resultado":0}]
    prom = promedio(attribute)
    operacion = ((prom)*(float(element_1[0])**2))/float(element_2[0])

    redondear = round(operacion,2)
    resultado = [{"resultado":redondear,"decorador":"%"}]
    return resultado