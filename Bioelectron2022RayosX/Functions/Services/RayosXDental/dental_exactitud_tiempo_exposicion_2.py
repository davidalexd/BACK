def dental_exactitud_tiempo_exposicion_2(element_1,element_2):
    # llama a TIEMPO DE EXPOSICIÓN (s) y luego a TIEMPO (s) in range 1
    resultado =  [{"resultado":0}]
    element_a = float(element_1[0])
    element_b = float(element_2[0])

    operacion = (element_a-element_b)/element_a

    redondeo = round(operacion,2)
    tolerancia_1 = 10
    tolerancia = True

    if (redondeo <= tolerancia_1*2 or redondeo <=tolerancia_1):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado