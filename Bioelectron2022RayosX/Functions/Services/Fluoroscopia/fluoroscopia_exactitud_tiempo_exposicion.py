from Functions.Services.promedio import promedio

def fluoroscopia_exactitud_tiempo_exposicion(element_1,attributes):
    resultado = 0
    prom = promedio(attributes)
    operacion = ((element_1[0]-prom)/element_1[0])*100
    redondear = round(operacion,2)
    resultado = [{"resultado":redondear,"decorador":"%"}]
    return resultado