def tomografia_valor_medio_numero_ct(element_1,element_2):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    tolerancia_1 = True
    tolerancia_2 = False

    redondear_1 = round(float(element_1[0]))
    redondear_2 = round(float(element_2[0]))

    tolerancia_a_1 = 4
    tolerancia_a_2 = -4

    tolerancia_b_1 = -1004
    tolerancia_b_2 = 996

    if(redondear_1<tolerancia_a_1 or redondear_1<tolerancia_a_2):
        tolerancia_1 = True
    else:
        tolerancia_1 = False

    if(redondear_2<tolerancia_b_1 or redondear_2<tolerancia_b_2):
        tolerancia_2 = True
    else:
        tolerancia_2 = False

    resultado = [
        {"parametros":"","resultado":redondear_1,"condicion":tolerancia_1},
        {"parametros":"","resultado":redondear_2,"condicion":tolerancia_2}
    ]

    return resultado
    