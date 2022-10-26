from Functions.Services.promedio import promedio
def dental_kerma_aire_entrada_paciente(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)

    operacion = (prom/1000)*1.1

    redondeo=round(operacion,2)

    tolerancia = True

    if (redondeo < 4):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondeo)+" mGy","condicion":tolerancia}],"tolerancia":"Deberá ser inferior a 4 mGy "}

    return resultado