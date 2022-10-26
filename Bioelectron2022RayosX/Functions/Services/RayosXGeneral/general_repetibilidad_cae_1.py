from Functions.Services.promedio import promedio

def general_repetibilidad_cae_1(attribute=[0],element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    tolerancia = True

    operacion = (float(element[0])-prom)/float(element[0])

    redondear = round(operacion,2)

    if(redondear <= 20 or redondear <=-20):
        tolerancia = True
    else:
        tolerancia = False
    
    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":"≤± 20"}

    return resultado