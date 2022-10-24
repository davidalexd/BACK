from Functions.Services.promedio import promedio


def fluoroscopia_filtracion_capa_hemireductora(attributes=[0],element=[0]):
        resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
        prom = promedio(attributes)
        redondear = round(prom,2)
        tolerancia=True
        tolerancia_1=2.9

        if(float(element[0])==70):
                tolerancia_1=2.5
        else:
                tolerancia_1=2.9

        if(redondear>tolerancia_1):
                tolerancia=True
        else:
                tolerancia=False


        resultado = {"data":[{"parametros":"","resultado":str(redondear)+"mmAl","condicion":tolerancia}],"tolerancia":"> 2.5 mmAl (a 70 kVp) y >2.9 mmAl (a 80 kVp)"}
        
        return resultado