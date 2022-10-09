from resta import resta
from functools import reduce

def resta_range(attributes):
    resultado = 0
    resultado = {"valor":reduce(resta, attributes)}
    return resultado