from promedio import promedio as prom

def valor_rendimiento(attributes,element_a,element_b,element_c):
    promedio = prom(attributes)
    valor_rendimiento = (promedio(*element_a**2))/(element_b*element_c)
    resultado = {"valor":valor_rendimiento}
    return resultado