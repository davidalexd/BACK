from Functions.Services.promedio import promedio
def dental_filtracion(attribute):
    resultado =  [{"resultado":0}]
    prom = promedio(attribute)

    redondeo=round(prom,2)

    tolerancia = True
    if (redondeo >= 10):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo)+" mm Al",
            "condicion":tolerancia
        }
    ]
    return resultado
