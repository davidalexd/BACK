def fluoroscopia_alineacion_rayos_x_haz_luminoso(element_1,element_2,element_3,element_4):
    resultado = [{"resultado":0}]
    datos_suma = [0]
    datos_suma = [float(element_1[0]),float(element_2[0]),float(element_3[0]),float(element_4[0])]
    resultado = [
        {
            "resultado":sum(datos_suma),
            "decorador":"cm"
        }
    ]
    return resultado