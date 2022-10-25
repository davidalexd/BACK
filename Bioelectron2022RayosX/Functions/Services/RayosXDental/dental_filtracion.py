from Functions.Services.promedio import promedio
def dental_filtracion(attribute=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attribute)
    redondeo=round(prom,2)

    tolerancia = True
    if (redondeo >= 1.5):
        tolerancia = True
    else:
        tolerancia = False

    resultado = {"data":[{"parametros":"","resultado":str(redondeo)+" mm Al","condicion":tolerancia}],"tolerancia":"Filtración total mayor o igual que 1.5 mm Al "}

    return resultado
