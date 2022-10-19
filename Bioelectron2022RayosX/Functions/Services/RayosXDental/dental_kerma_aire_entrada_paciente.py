from Functions.Services.promedio import promedio
def dental_kerma_aire_entrada_paciente(attribute):
    resultado = [{"resultado":0}]
    prom = promedio(attribute)

    operacion = (prom/1000)*1.1

    redondeo=round(operacion,2)

    tolerancia = True

    if (redondeo < 4):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo),
            "condicion":tolerancia
        }
    ]
    return resultado