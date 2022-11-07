from Functions.Services.validacion import validacion

def mamografia_distancia_foco_película_detector_imagen(element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

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
                "resultado":redondear+" cm",
                "estado":tolerancia
            },
        ]
        ,
        "tolerancia":"≥60 cm",
        "estado":estado
        }
    
    return resultado