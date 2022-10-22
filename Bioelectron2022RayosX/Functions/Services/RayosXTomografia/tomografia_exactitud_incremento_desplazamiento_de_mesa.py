def tomografia_exactitud_incremento_desplazamiento_de_mesa(element_1=[0],element_2=[0]):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    
    tolerancia =True
    operacion = float(element_1[0])-float(element_2[0])
    redondear = round(operacion,2)

    tolerancia_1 = 1
    tolerancia_2 = -1

    if(redondear <= tolerancia_1 or redondear <= tolerancia_2):
        tolerancia = True
    else:
        tolerancia = False

    resultado = [
         {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado