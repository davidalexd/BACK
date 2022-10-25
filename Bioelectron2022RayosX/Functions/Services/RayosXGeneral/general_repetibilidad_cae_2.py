from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def general_repetibilidad_cae_2(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    tolerancia = True

    operacion = float(element_1[0])-float(element_2[0])/float(element_1[0])

    redondear = round(operacion,2)
    
    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":""}

    return resultado