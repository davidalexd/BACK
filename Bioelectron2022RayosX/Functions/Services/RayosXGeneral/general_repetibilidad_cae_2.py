from Functions.Services.promedio import promedio
from Functions.Services.valor_absoluto import valor_absoluto

def general_repetibilidad_cae_2(attribute=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    tolerancia = True

    operacion = valor_absoluto((float(element_2[0])-prom)/float(element_2[0]))

    redondear = round(operacion*100,2)

    if(redondear <= 20 or redondear <=-20):
        tolerancia = True
    else:
        tolerancia = False
    
    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"≤± 20"}

    return resultado