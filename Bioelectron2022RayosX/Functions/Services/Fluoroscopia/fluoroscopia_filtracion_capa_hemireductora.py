from Functions.Services.promedio import promedio


def fluoroscopia_filtracion_capa_hemireductora(attributes):
    resultado = [{"resultado":0}]
    prom = promedio(attributes)
    redondear = round(prom,2)
    resultado = [{"resultado":redondear,"decorador":"mmAl"}]
    return resultado