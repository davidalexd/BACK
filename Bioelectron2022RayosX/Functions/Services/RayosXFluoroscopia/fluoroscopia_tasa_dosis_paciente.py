from Functions.Services.validacion import validacion

def fluoroscopia_tasa_dosis_paciente(element_1,element_2):
    try:
        tolerancia_1 = True
        tolerancia_2 = True
        operacion_1 = float(element_1[0])*60/1000
        operacion_2 = float(element_2[0])*60/1000
        redondear_1 = round(operacion_1,2)
        redondear_2 = round(operacion_2,2)

        if(redondear_1<=50):
            tolerancia_1 = True
        else:
            tolerancia_1 = False
        if(redondear_2<=100):
            tolerancia_2 = True
        else:
            tolerancia_2 = False
        
        estado = validacion([tolerancia_1,tolerancia_2])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear_1)+" mGy/min",
                    "estado":tolerancia_1
                },
                {
                    "parametros":"",
                    "resultado":str(redondear_2)+" mGy/min",
                    "estado":tolerancia_2
                }
            ],
            "tolerancia":"≤ 50 mGy/min. y ≤ 100 mGy/min.",
            "estado":estado
            }


        return resultado
    except Exception as e:
                        resultado = {
                        "condicion":"",
                        "data":[
                                {
                                "parametros":"",
                                "resultado":"",
                                "estado":""
                                }
                        ],
                        "tolerancia":"",
                        "estado":"No Aplica"
                        }
                        return resultado