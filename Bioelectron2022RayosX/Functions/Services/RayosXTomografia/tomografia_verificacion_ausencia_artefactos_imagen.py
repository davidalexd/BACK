from Functions.Services.validacion import validacion

def tomografia_verificacion_ausencia_artefactos_imagen(opcion):
    try:
        tolerancia = True

        if(opcion[0]=="Ausencia de artefactos"):
            tolerancia = True  
        else:
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
            "tolerancia":"No se deben apreciar artefactos en las imágenes de tomografía.",
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