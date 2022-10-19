def fluoroscopia_alineacion_rayos_x_haz_luminoso(element_1,element_2,element_3,element_4,element_5):
    resultado = [{"resultado":0}]
    datos_suma = [0]
    datos_suma = [float(element_1[0]),float(element_2[0]),float(element_3[0]),float(element_4[0])]
    parametro = ("L1 - "+str(element_1[0])+"% , L2 - "+str(element_2[0])+"%, L3 - "+str(element_3[0])+"% , L4 - "+str(element_4[0])+"%")
    operacion = sum(datos_suma)
    redondear = round(operacion,2)

    tolerancia = True
    tolerancia_1 = (3*float(element_5[0])/100)
    tolerancia_2 = (2*float(element_5[0])/100)

    if (redondear <= tolerancia_1 and redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False
    # if (redonder<=2.4):

    resultado = [
        {
            "parametros":parametro,
            "resultado":"Suma total = "+str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado