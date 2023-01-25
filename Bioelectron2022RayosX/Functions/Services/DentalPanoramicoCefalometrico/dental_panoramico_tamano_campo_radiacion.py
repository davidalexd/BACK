from Functions.Services.validacion import validacion

def dental_panoramico_tamano_campo_radiacion(opcion):
    try:
        if(opcion[0]=="El campo de radiación no excede las dimensiones del receptor de imagen"):
            tolerancia = True
        if(opcion[0]=="El campo de radiación excede las dimensiones del receptor de imagen"):
            tolerancia = False
        if(opcion[0]=="El campo de radiación está ajustado a las dimensiones de los detectores"):
            tolerancia = True
        if(opcion[0]=="El campo de radiación no está ajustado a las dimensiones de los detectores"):
            tolerancia = False
            
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":opcion,
                    "estado":tolerancia
                }
            ],
            "tolerancia":"En cefalometría, el tamaño del campo de radiación no debe exceder las dimensiones del receptor de imagen. En sistemas digitales directos de barrido, el campo de radiación debe estar ajustado a las dimensiones de los detectores. ",
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
