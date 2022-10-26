from Functions.Services.suma_range import suma_range


def general_alineación_rayos_X_haz_luminoso(attribute=[0],element=[0]):
    # attribute = Diferencia entre bordes (cm):
    # element = Distancia al Foco-Sistema de colimacion (cm):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    suma = suma_range(attribute)

    tolerancia_1 = True
    tolerancia_2 = True

    redondear = round(suma,2)

    if(redondear<=(3*float(element[0])/100)):
        tolerancia_1 = True
    else:
        tolerancia_1 = False

    if(redondear< 2 or redondear<-2):
        tolerancia_2 = True
    else:
        tolerancia_2 = False

    resultado = {"data":[
        {"parametros":"","resultado":redondear,"condicion":tolerancia_1},
        {"parametros":"","resultado":redondear,"condicion":tolerancia_2}
        ]
        ,"tolerancia":"Suma de las desviaciones absolutas en los bordes inferiores al ± 2% de la distancia entre el foco y el maniquí de colimación para cada dirección principal. La suma total de las desviaciones absolutas no excederá, por otra parte, el 3% de la distancia entre el foco y maniquí de colimación."}
    
    return resultado