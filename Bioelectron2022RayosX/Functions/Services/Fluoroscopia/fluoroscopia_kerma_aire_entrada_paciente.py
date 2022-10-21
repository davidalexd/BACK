from Functions.Services.promedio import promedio

def fluoroscopia_kerma_aire_entrada_paciente(attributes,element,select_tolerancia):
    resultado = [{"resultado":0}]
    tolerancia = True
    prom=promedio(attributes)
    operacion = prom*float(element[0])**2
    redondeo= round(operacion,2)

    if(redondeo<float(select_tolerancia["valor"])):
        tolerancia = True
    else:
        tolerancia = False
    
    resultado = [{
            "parametros":"",
            "resultado":redondeo,
            "condicion":tolerancia
    }]

    return resultado