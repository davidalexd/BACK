from Functions.Services.validacion import validacion

def mamografia_perdida_imagen_pared_torax(element):
    try:
        tolerancia = True

        if(float(element[0])<=5):
            tolerancia = True
        else:
            tolerancia = False
        
        
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":element[0]+"mm",
                    "estado":tolerancia
                },
            ]
            ,"tolerancia":"Anchura de la imagen perdida ≤±5mm",
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