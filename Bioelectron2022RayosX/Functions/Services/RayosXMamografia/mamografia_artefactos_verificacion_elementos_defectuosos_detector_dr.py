from Functions.Services.validacion import validacion

def mamografia_artefactos_verificacion_elementos_defectuosos_detector_dr(opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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
