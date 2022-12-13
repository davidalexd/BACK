from Functions.Services.validacion import validacion

def mamografia_artefactos_cr(opcion):
    try:
        tolerancia = True

        if(opcion[0] == "SIN ARTEFACTOS"):
            tolerancia = True
        else:
            tolerancia = False
        
        
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":opcion[0],
                    "estado":tolerancia
                },
            ]
            ,"tolerancia":"SIN ARTEFACTOS",
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