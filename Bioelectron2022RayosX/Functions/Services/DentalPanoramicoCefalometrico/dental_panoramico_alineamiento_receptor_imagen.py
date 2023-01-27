from Functions.Services.validacion import validacion

def dental_panoramico_alineamiento_receptor_imagen(opcion):
    try:
        if(opcion[0]=="El haz de radiación coincide con la rendija de entrada"):
            tolerancia = True
        if(opcion[0]=="El haz de radiación no coincide con la rendija de entrada"):
            tolerancia = False
        if(opcion[0]=="El haz de radiación irradia la fila de detectores de forma centrada"):
            tolerancia = True
        if(opcion[0]=="El haz de radiación no irradia la fila de detectores de forma centrada"):
            tolerancia = False
            
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":opcion[0],
                    "estado":tolerancia
                }
            ],
            "tolerancia":"En modo panorámico con sistema de película, el haz de radiación debe coincidir con la rendija de entrada al receptor de imagen. En sistemas digitales directos, tanto en panorámicas como en cefalometría, el haz de radiación debe irradiar la fila de detectores de forma centrada. ",
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
