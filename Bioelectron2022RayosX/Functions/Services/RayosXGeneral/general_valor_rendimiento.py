from Functions.Services.promedio import promedio

def general_valor_rendimiento(element_1=[0],attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    operacion = prom/float(element_1[0])
    redondear = round(operacion,2)
    tolerancia=True

    if(redondear > 3 and redondear < 65):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"De modo orientativo, a 80 kV y con una filtración estimada entre 2.5 y 5 mmAl, el rendimiento estará entre 30 y 65 uGy/mAs a 1 m del foco"}

    return resultado