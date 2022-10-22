from Functions.Services.promedio import promedio

def fluoroscopia_exactitud_tension(element_1,attributes):
        resultado = 0
        prom = promedio(attributes)
        operacion = ((float(element_1[0])-prom)/float(element_1[0]))*100
        redondear = round(operacion,2)
        tolerancia = True
        tolerancia_1 = 10
        tolerancia_2 = -10

        if(redondear < tolerancia_1 or redondear < tolerancia_2):
                tolerancia = True
        else:
                tolerancia = False


        resultado = [{
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        }]
        return resultado