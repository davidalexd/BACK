
def dental_variacion_rendimiento(element_1,element_2,element_3,element_4,element_5,element_6):
    resultado =  [{"resultado":0}]
    varaicion_1 = float(element_1[0])*(float(element_2[0])*2)
    varaicion_2 = float(element_3[0])*(float(element_4[0]))
    varaicion_3 = float(element_5[0])*(float(element_2[0])*2)
    varaicion_4 = float(element_6[0])*(float(element_3[0]))
    operacion_1 = (varaicion_1/varaicion_2)-varaicion_3/varaicion_4
    operacion_2 = (varaicion_1/varaicion_2)+varaicion_3/varaicion_4

    operacion = operacion_1/operacion_2

    redondeo = round(operacion,2)

    tolerancia = True

    if(redondeo <= 0.1):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondeo),
            "condicion":tolerancia
        }
    ]
    return resultado