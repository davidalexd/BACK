from Functions.Services.validacion import validacion

def mamografia_distancia_foto_detector_imagen(element):
    try:

        redondear = round(float(element[0]),2)
        tolerancia = True
        
        if(redondear>=60):
            tolerancia = True
        else:
            tolerancia= False


        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" cm",
                    "estado":tolerancia
                },
            ]
            ,
            "tolerancia":"≥60 cm",
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