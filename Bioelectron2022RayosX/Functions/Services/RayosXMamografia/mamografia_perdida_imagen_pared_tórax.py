from Functions.Services.validacion import validacion

def mamografia_perdida_imagen_pared_tórax(element=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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
                "resultado":float(element[0])+" ,,",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":"≤±5%",
        "estado":estado
        }
    

    return resultado