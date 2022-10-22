from Functions.Services.promedio import promedio
def fluoroscopia_tasa_dosis_maxima_entrada_intensificador_imagen(element,attribute):
    resultado = [{"resultado":0}]
    tolerancia = True
    prom=promedio(attribute[0])
    operacion = ((prom-float(element[0]))/prom)*100
    redondeo = round(operacion,2)
    tolerancia_1 = 20
    tolerancia_2 = -20
    if(redondeo<tolerancia_1 or redondeo<tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False
        
    resultado = [{
            "parametros":"",
            "resultado":redondeo,
            "condicion":tolerancia
    }]

    return resultado