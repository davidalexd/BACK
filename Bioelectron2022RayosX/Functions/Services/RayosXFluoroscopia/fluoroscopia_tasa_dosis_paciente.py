def fluoroscopia_tasa_dosis_paciente(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    tolerancia_1 = True
    tolerancia_2 = True
    operacion_1 = float(element_1[0])*60/1000
    operacion_2 = float(element_2[0])*60/1000
    redondear_1 = round(element_1,2)
    redondear_2 = round(element_2,2)

    if(redondear_1<=50):
        tolerancia_1 = True
    else:
        tolerancia_1 = False
    if(redondear_2<=100):
        tolerancia_2 = True
    else:
        tolerancia_2 = False
    
    resultado = {"data":[
        {
            "parametros":"",
            "resultado":str(redondear_1),
            "condicion":tolerancia_1
        },
        {
            "parametros":"",
            "resultado":str(redondear_2),
            "condicion":tolerancia_2
        }
        ],"tolerancia":"≤ 50 mGy/min. y ≤ 100 mGy/min."}


    return resultado