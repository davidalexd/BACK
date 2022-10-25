def general_dosis_superficie_paciente(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    operacion = float(element_1[0])/(1000*(float(element_2[0])**2))
    redondear = round(operacion,2)
    tolerancia=True

    if(redondear<0.4):
        tolerancia=True
    else:
        tolerancia=False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+" mGy","condicion":tolerancia}],"tolerancia":"0.4 mGy "}

    return resultado