from Functions.Services.promedio import promedio


def general_filtracion(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    redondear = round(prom,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado