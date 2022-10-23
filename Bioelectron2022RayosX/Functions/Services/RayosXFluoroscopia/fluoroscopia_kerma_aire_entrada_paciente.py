from Functions.Services.promedio import promedio

def fluoroscopia_kerma_aire_entrada_paciente(attribute_1=[0],attribute_2=[0],attribute_3=[0],element=[0],opcion=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    tolerancia = True
    prom=promedio([attribute_1[0],attribute_2[0],attribute_3[0]])
    operacion = prom*float(element[0])**2
    redondeo= round(operacion,2)

    if(redondeo<float(opcion[0])):
        tolerancia = True
    else:
        tolerancia = False
    
    resultado = {"data":[{"parametros":"","resultado":redondeo,"condicion":tolerancia}],"tolerancia":"<"+opcion[0]+"mGy"}

    return resultado