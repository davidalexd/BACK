def variacion_rendimiento(element_a,element_b,element_c,element_d,element_e):
    rendimiento_a = ((element_a*(element_b**2))/(element_c*element_b))
    rendimiento_b = ((element_d*(element_b**2))/(element_e*element_b))
    variacion_rendimiento = (rendimiento_a-rendimiento_b)/(rendimiento_a+rendimiento_b)
    resultado = {"valor":variacion_rendimiento}
    return resultado
