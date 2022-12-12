from Functions.Services.validacion import validacion

def mamografia_dosis_superficie_mama(element_1,element_2,element_3,opcion):
    try:
        tolerancia = True
        operacion = element_1*element_2*element_3
        
        tolerancia_valor = 10

        if(opcion[0] == "SÍ"):
            tolerancia_valor = 10
        else:
            tolerancia_valor = 4
        
        if(operacion <= tolerancia_valor):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":operacion+" mGy",
                    "estado":tolerancia
                },
            ]
            ,"tolerancia":"≤ 4 mGy sin rejilla y ≤ 10 mGy con rejilla",
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
        