def fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen(element):
    resultado = [{"resultado":0}]
    redondear = round(element[0],2)

    
    tolerancia = True
    if(redondear<=1.5):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"º",
            "condicion":tolerancia
        }
    ]

    return resultado