from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m

def fluoroscopia_repetibilidad_cai(attribute_1=[0],attribute_2=[1],attribute_3=[2]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    desv = desviacion_estandar_m([attribute_1[0],attribute_2[0],attribute_3[0]])
    prom = promedio([attribute_1[0],attribute_2[0],attribute_3[0]])
    tolerancia = True
    if(prom == 0):
        operacion = 0
    else:
        operacion = desv/prom
        
    redondear = round(operacion,2)
    
    if(redondear<=10):
        tolerancia = True
    else:
        tolerancia = False


    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":"Coeficiente de variación ≤ 10%"}


    return resultado
