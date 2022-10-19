def fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen(element):
    resultado = [{"resultado":0}]
    redondear = round(element[0],2)
    resultado = [
        {
            "resultado":redondear,
            "decorador":"º"
        }
    ]

    return resultado