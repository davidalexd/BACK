from desviacion_estandar_m import desviacion_estandar_m

def repetibilidad_rendimiento(attributes,element_a,element_b):
    desviacion_estandar = desviacion_estandar_m(attributes)
    repetibilidad_rendimiento = (desviacion_estandar*(element_a**2))/element_b
    resultado = {"valor":repetibilidad_rendimiento}
    return resultado