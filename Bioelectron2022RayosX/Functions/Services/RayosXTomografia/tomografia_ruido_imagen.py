from Functions.Services.desviacion_estandar_m import desviacion_estandar_m


def tomografia_ruido_imagen(attributes=[0],opcion=[0]):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    tolerancia =True
    desv = desviacion_estandar_m(attributes)
    redondear = round(desv,2)

    if(desv<=float(opcion[0])):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondear)+"UH",
            "condicion":tolerancia
        }
    ]
    return resultado


