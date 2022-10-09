from promedio import promedio as prom

def filtracion(attributes):
    promedio = prom(attributes)
    filtracion = promedio
    resultado = {"valor":filtracion}
    return resultado