from Functions.Services.promedio import promedio


def general_filtracion(attributes=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    prom = promedio(attributes)
    redondear = round(prom,2)
    tolerancia=True

    if(redondear > 2.5):
        tolerancia=True
    else:
        tolerancia=False

    resultado = {"data":[{"parametros":"","resultado":str(redondear)+"mmAl","condicion":tolerancia}],"tolerancia":"Filtración > 2.5 mm equivalentes de aluminio"}

    return resultado