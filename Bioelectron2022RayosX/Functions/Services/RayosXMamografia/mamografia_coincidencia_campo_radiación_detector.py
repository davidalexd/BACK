from Functions.Services.validacion import validacion

def mamografia_coincidencia_campo_radiación_detector(element):
    try:

        redondear = round(float(element[0]),2)
        tolerancia = True
        
        if(redondear<=5):
            tolerancia = True
        else:
            tolerancia= False


        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":"El campo de rayos X cubre toda el área del detector sobrepasando "+str(redondear)+" mm el lado que corresponde a la pared del tórax",
                    "estado":tolerancia
                },
            ]
            ,
            "tolerancia":"El campo de rayos X deberá cubrir toda el área activa del detector sin sobrepasar el soporte de la mama o tablero en ningún lado a excepción del correspondiente a la pared del tórax que podrá sobrepasar en una cantidad inferior o igual a 5 mm.",
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