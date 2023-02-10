from Functions.Services.validacion import validacion

def general_dosis_superficie_paciente(element_1,element_2):
    try:
        if(float(element_2[0])==0):
            operacion = 0
        else:
            operacion = float(element_1[0])/(1000*(float(element_2[0])**2))
               
        redondear = round(operacion,2)
        tolerancia=True

        if(redondear<0.4):
            tolerancia=True
        else:
            tolerancia=False

        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" mGy",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"0.4 mGy ",
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