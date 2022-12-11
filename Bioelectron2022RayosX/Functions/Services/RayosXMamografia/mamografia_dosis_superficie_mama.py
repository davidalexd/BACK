from Functions.Services.validacion import validacion

def mamografia_dosis_superficie_mama(element_1=[0],element_2=[0],element_3=[0],opcion=[""]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
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
        