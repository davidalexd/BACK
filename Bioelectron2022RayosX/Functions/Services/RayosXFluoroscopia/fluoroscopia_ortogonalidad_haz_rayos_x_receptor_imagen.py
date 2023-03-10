from Functions.Services.validacion import validacion

def fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen(element):
    try:
        redondear = round(float(element[0]),2)        
        tolerancia = True
        if(redondear<=1.5):
            tolerancia = True
        else:
            tolerancia = False
            
        estado = validacion([tolerancia])


        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"º",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°.",
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