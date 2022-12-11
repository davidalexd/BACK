from Functions.Services.validacion import validacion

def mamografia_resolucion_espacial(element_1=[0],element_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    element = float(element_2[0])
    tolerancia = True
    tolerancia_valor = 0.8*((1/(2*float(element_1[0])))*1000)

    if(element > tolerancia_valor):
        tolerancia = True
    else:
        tolerancia = False

    
    estado = validacion([tolerancia])

    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":element+"pl/mm",
                "estado":tolerancia
            },
        ]
        ,"tolerancia":">"+ tolerancia_valor+"% de la frecuencia de Nyquist",
        "estado":estado
        }
        
    return resultado 

