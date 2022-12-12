from Functions.Services.validacion import validacion

def dental_tamano_campo_extremo_localizador(element):
    try:
        # llama Tamaño de Campo
        operacion = float(element[0])
        redondear = round(operacion,2)

        tolerancia = True

        if (redondear <= 6):
            tolerancia = True
        else:
            tolerancia = False

        estado = validacion([tolerancia])
            
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+"cm",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"≤6 cm",
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