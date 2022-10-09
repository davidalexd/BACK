from promedio import promedio as prom
def inversion_cuadrados(distancia,attributes):
    promedio = prom(attributes)
    inversion_cuadrado = promedio*(distancia**2)/100**2
    resultado = {"valor":inversion_cuadrado}
    return resultado
