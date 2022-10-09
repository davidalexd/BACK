from promedio import promedio as prom
def exactitud_tension(element,attributes):
    promedio = prom(attributes)
    exactitud_tension = (element-promedio)/element
    resultado = {"valor":exactitud_tension}
    return resultado
