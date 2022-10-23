from Functions.Services.promedio import promedio

def tomografia_filtracion_capa_hemirreductora(attribute=[0],element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    tolerancia = True
    operacion = float(element_1[0])-prom-float(element_2[0])
    redondear = round(operacion,2)
    tolerancia_1 = 1
    tolerancia_2 = -1

    if (redondear <= tolerancia_1 or redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":redondear,"condicion":tolerancia}],"tolerancia":"Según especificaciones del fabricante: (VM – VN) ≤ ±1 mmAl  "}
    
    return resultado
