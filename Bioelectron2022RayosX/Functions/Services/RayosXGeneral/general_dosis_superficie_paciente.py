def general_dosis_superficie_paciente(element_1,element_2):
    resultado = [{"resultado":0}]
    operacion = float(element_1[0])/(1000*(float(element_2[0])**2))
    redondear = round(operacion,2)
    tolerancia=True
    
    resultado = [
        {
            "parametros":"",
            "resultado":str(redondear)+"%",
            "condicion":tolerancia
        }
    ]
    return resultado