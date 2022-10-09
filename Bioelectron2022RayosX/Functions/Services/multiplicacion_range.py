from multiplicacion import multiplicacion
from functools import reduce

def multiplicacion_range(attributes):
    resultado = 0
    resultado = {"valor":reduce(multiplicacion.multiplicacion, attributes)}
    return resultado