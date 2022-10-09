from datetime import datetime
def intervalo_tiempo(tiempo_referencia):
    tiempo_inicial = datetime.strptime(tiempo_referencia, "%m/%d/%Y")
    tiempo_final= datetime.now()
    intervalo = (tiempo_final-tiempo_inicial).days
    resultado = {"valor":intervalo}
    return resultado
    