from Functions.Services.promedio import promedio
def fluoroscopia_compensacion_diferentes_espesores(attribute_1,attribute_2):
    ordenador = [0,1,2]
    tolerancia=True
    tolerancia_1 = 20
    tolerancia_2 = -20
    Uc = []
    for x in ordenador:
        element_1 = float(attribute_1[x])
        prom = promedio(attribute_2[x])

        operacion = (element_1-prom)*100/element_1
        redondeo = round(operacion,2)   
        
        if(redondeo <=tolerancia_1 or redondeo<=tolerancia_2):
            tolerancia=True
        else:
            tolerancia=False


        Uc.append({
            "parametros":"",
            "resultado":redondeo,
            "condicion":tolerancia
        })
        
    resultado = Uc

    return resultado
        

