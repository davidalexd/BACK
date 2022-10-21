from Functions.Services.promedio import promedio

def fluoroscopia_compensacion_cae(element,attribute_1,attribute_2):
    resultado = [{"resultado":0}]

    prom_1 = promedio(attribute_1)
    prom_2 = promedio(attribute_2)
    tolerancia_1 = True
    tolerancia_2 = True

    operacion_1 = (float(element[0])-prom_1)/float(element[0])
    operacion_2 = (float(element[0])-prom_2)/float(element[0])

    redondear_1 = round(operacion_1,2)
    redondear_2 = round(operacion_2,2)

    tolerancia_a = 15
    tolerancia_b = -15

    if(redondear_1<tolerancia_a or redondear_1<tolerancia_b):
        tolerancia_1 = True
    else:
        tolerancia_1 = False

    if(redondear_2<tolerancia_a or redondear_2<tolerancia_b):
        tolerancia_2 = True
    else:
        tolerancia_2 = False

    result = [
        {
            "parametros":"",
            "resultado":redondear_1,
            "condicion":tolerancia_1
        },
        {
            "parametros":"",
            "resultado":redondear_2,
            "condicion":tolerancia_2
        }
    ]
    return result