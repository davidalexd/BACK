from Functions.Services.promedio import promedio
def fluoroscopia_valor_rendimiento(attribute,element_1,element_2):
        resultado = [{"resultado":0}]
        tolerancia = True
        prom = promedio(attribute)
        operacion = ((prom)*(float(element_1[0])**2))/float(element_2[0])
        redondear = round(operacion,2)

        if(redondear< 25):
                tolerancia = True
        else:
                tolerancia = False
                
        resultado = [{
                "parametros":"",
                "resultado":str(redondear)+"%",
                "condicion":tolerancia
        }]
        return resultado