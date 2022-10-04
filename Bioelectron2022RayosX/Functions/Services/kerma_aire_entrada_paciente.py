from promedio import promedio as prom

def kerma_aire_entrada_paciente(attributes):
    promedio = prom(attributes)
    kerma_aire_entrada_paciente = (promedio/1000)*1.2
    resultado = {"valor":kerma_aire_entrada_paciente}
    return resultado