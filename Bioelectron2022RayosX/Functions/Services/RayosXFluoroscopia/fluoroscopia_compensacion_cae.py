from Functions.Services.promedio import promedio
from Functions.Services.desviacion_estandar_m import desviacion_estandar_m
from Functions.Services.valor_absoluto import valor_absoluto


def fluoroscopia_compensacion_cae(opcion=[""],attribute_1=[0],attribute_2=[0],attribute_3=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    prom_3 = promedio([attribute_1[0],attribute_2[0],attribute_3[0]])


    prom_1= promedio([attribute_1[1],attribute_2[1],attribute_3[1]])
    operacion_1 = (float(attribute_1[0])-prom_1)/float(attribute_1[0])

    prom_2 = promedio([attribute_1[2],attribute_2[2],attribute_3[2]])
    operacion_2 = (float(attribute_1[0])-prom_2)/float(attribute_1[0])


    if(opcion[0]=="Medidas Indice de Exposicio"):
        operacion_3 = prom_3-prom_2
    else:
        operacion_3 = (prom_3-prom_2)*100/prom_3

    redondear_1 = round(operacion_1,2)
    redondear_2 = round(operacion_2,2)
    redondear_3 = round(operacion_3,2)


    abs_1 = valor_absoluto(operacion_1)
    abs_2 = valor_absoluto(operacion_2)
    abs_3 = valor_absoluto(operacion_3)

    if(opcion[0]=="Medidas Indice de Exposicio"):
        tolerancia_a_1 = 0.2
        tolerancia_b_1 = -0.2
        if(abs_1<=tolerancia_a_1 or abs_1<=tolerancia_b_1):
            tolerancia_1 = True
        else:
            tolerancia_1  = False
        if(abs_2<=tolerancia_a_1 or abs_2<=tolerancia_b_1):
            tolerancia_2 = True
        else:
            tolerancia_2  = False
        if(abs_3<=tolerancia_a_1 or abs_3<=tolerancia_b_1):
            tolerancia_3 = True
        else:
            tolerancia_3  = False
    else:
        tolerancia_a_1 = 15
        tolerancia_b_1 = -15
        if(abs_1<=tolerancia_a_1 or abs_1<=tolerancia_b_1):
            tolerancia_1 = True
        else:
            tolerancia_1  = False
        if(abs_2<=tolerancia_a_1 or abs_2<=tolerancia_b_1):
            tolerancia_2 = True
        else:
            tolerancia_2  = False
        if(abs_3<=tolerancia_a_1 or abs_3<=tolerancia_b_1):
            tolerancia_3 = True
        else:
            tolerancia_3  = False


    resultado = {"data":[
        {"parametros":"","resultado":redondear_1,"condicion":tolerancia_1},
        {"parametros":"","resultado":redondear_2,"condicion":tolerancia_2},
        {"parametros":"","resultado":redondear_3,"condicion":tolerancia_3}
        ],
        "tolerancia":"Desviación ± "+tolerancia_a_1+"%"}

    return resultado