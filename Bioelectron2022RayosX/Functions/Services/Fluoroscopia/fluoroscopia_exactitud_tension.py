from Functions.Services.promedio import promedio


def fluoroscopia_exactitud_tension(element_1,attributes):
    resultado = 0
    prom = promedio(attributes)
    operacion = ((float(element_1[0])-prom)/float(element_1[0]))*100
    redondear = round(operacion,2)
    resultado = [{"resultado":redondear,"decorador":"%"}]
    return resultado