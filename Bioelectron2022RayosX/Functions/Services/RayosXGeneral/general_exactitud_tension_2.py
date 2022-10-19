from Functions.Services.promedio import promedio


def general_exactitud_tension_2(attribute,element_1):
    resultado = [{"resultado":0}]
    prom = promedio(attribute)
    operacion = (prom-float(element_1[0]))/prom
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado