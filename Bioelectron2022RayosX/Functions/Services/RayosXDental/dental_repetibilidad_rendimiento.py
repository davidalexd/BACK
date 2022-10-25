from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.RayosXDental.dental_valor_rendimiento import dental_valor_rendimiento

def dental_repetibilidad_rendimiento(attribute=[0],element_1=[0],element_2=[0],element_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    print(attribute,element_1,element_2,element_3)
    dvr = dental_valor_rendimiento(attribute,element_1,element_2,element_3)["data"][0]["resultado"]
    print(attribute)
    desvm = desviacion_estandar_m(attribute)
    variante_1 = float(element_1[0])*2

    operacion = (desvm*variante_1)/float(dvr)

    redondeo = round(operacion,2)

    tolerancia = True

    if(redondeo < 10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondeo)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación < 10% "}

    return resultado