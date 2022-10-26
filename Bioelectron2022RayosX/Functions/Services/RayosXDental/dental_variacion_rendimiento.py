
def dental_variacion_rendimiento(element_1=[0],element_2=[0],element_3=[0],element_4=[0],element_5=[0],element_6=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    variacion_1 = float(element_4[0])*(float(element_2[0])*2)
    variacion_2 = float(element_3[0])*(float(element_1[0]))
    variacion_3 = float(element_6[0])*(float(element_2[0])*2)
    variacion_4 = float(element_5[0])*(float(element_1[0]))

    print(variacion_1,variacion_2,variacion_3,variacion_4,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    
    operacion_1 = (variacion_1/variacion_2)-variacion_3/variacion_4
    operacion_2 = (variacion_1/variacion_2)+variacion_3/variacion_4
    
    operacion = operacion_1/operacion_2
    redondeo = round(operacion,2)
    tolerancia = True

    if(redondeo <= 0.1):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondeo),"condicion":tolerancia}],"tolerancia":"Coeficiente de linealidad menor o igual que 0.1 entre pasos consecutivos"}

    return resultado