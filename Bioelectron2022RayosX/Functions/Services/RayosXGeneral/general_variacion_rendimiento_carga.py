from Functions.Services.promedio import promedio

def general_variacion_rendimiento_carga(attributes,element_1,element_2,element_3):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    variante_1 = prom/element_1
    operacion = (variante_1-float(element_2[0])/float(element_3[0]))/(variante_1+float(element_2[0])/float(element_3[0]))
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear),
            "condicion":tolerancia
        }
    ]
    return resultado