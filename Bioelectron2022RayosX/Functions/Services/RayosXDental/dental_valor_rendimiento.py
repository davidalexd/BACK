from Functions.Services.promedio import promedio
def dental_valor_rendimiento(attribute=[0],element_1=[0],element_2=[0],element_3=[0]):
    print(attribute)
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    variante_1 = float(element_3[0])*2
    variante_2 = float(element_2[0])*float(element_1[0])

    operacion = (prom*variante_1)/variante_2

    redondeo = round(operacion,2)

    tolerancia = True

    if(redondeo > 25):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":redondeo,"condicion":tolerancia}],"tolerancia":"Superior a 25 uGy/mAs a 1 m del foco y a la tensión de disparo "}

    return resultado