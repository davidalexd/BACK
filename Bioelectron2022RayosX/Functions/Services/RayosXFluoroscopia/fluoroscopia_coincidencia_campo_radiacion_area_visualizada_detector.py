def fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector(element_1,element_2):
    resultado=[{"resultado":0}]
    operacion=(float(element_1[0])**2)/(float(element_2[0])**2)
    redondear = round(operacion,2)
    tolerancia = True
    if(redondear<=1.15):
        tolerancia = True
    else:
        tolerancia = False

    resultado=[
        {
            "parametros":"",
            "resultado":redondear,
            "condicion":tolerancia
        }
    ]
    return resultado