def tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado(element_1,element_2):
    resultado = [{"parametros":"","resultado":0,"condicion":True}]
    operacion = float(element_1[0])+float(element_2[0])
    tolerancia =True
    redondear = round(operacion,2)
    
    if(redondear <= 2):
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