from Functions.Services.promedio import promedio

def general_valor_rendimiento(attributes,element_1):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    operacion = prom/float(element_1[0])
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