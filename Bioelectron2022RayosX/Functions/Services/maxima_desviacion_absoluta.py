from Functions.Services.valor_maximo import valor_maximo
from Functions.Services.valor_minimo import valor_minimo

def maxima_desviacion_absoluta(attribute):
    max = valor_maximo(attribute)
    min = valor_minimo(attribute)

    for x in attribute:
        if max < float(x):
            max = float(x)
        
        if min > float(x):
            min = float(x)
        
    MaxDesvAbs = max - min

    return MaxDesvAbs