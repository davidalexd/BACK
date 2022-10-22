from Functions.Services.promedio import promedio


def fluoroscopia_filtracion_capa_hemireductora(attributes):
        resultado = [{"resultado":0}]
        prom = promedio(attributes)
        redondear = round(prom,2)
        tolerancia=True

        if(redondear>2.9):
                tolerancia=True
        else:
                tolerancia=False

        resultado = [{
            "parametros":"",
            "resultado":redondear+"mmAl",
            "condicion":tolerancia
        }]
        
        return resultado