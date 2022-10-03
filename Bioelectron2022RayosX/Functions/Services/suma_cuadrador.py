def suma_cuadrados(attributes):
    suma_cuadrados = 0
    for x in attributes:
        cuadrado = float(x)**2
        suma_cuadrados = cuadrado+suma_cuadrados
    resultado = {"valor":suma_cuadrados}
    return resultado