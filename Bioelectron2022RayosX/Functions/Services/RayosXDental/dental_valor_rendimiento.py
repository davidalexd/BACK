from Functions.Services.promedio import promedio
def dental_valor_rendimiento(attribute,element_1,element_2,element_3):
    resultado =  [{"resultado":0}]
    prom = promedio(attribute)
    variante_1 = float(element_1[0])*2
    variante_2 = float(element_2[0])*float(element_3[0])

    operacion = (prom*variante_1)/variante_2

    redondeo = round(operacion,2)

    tolerancia = True

    if(redondeo > 25):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":redondeo,
            "condicion":tolerancia
        }
    ]
    return resultado