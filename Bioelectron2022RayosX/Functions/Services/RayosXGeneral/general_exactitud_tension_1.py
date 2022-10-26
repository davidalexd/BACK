def general_exactitud_tension_1(element_1=[0],element_2=[0]):
    # element_1 = TENSION #1
    # element_2 = TENSION PROMEDIO

    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = (float(element_2[0])-float(element_1[0]))/float(element_1[0])
    redondear = round(operacion,2)*100
    tolerancia=True
    
    if(redondear< 10 or redondear < -10):
        tolerancia=True
    else:
        tolerancia=False


    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"%","condicion":tolerancia}],"tolerancia":""}

    return resultado