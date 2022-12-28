from Functions.Services.validacion import validacion

def tomografia_coincidencia_indicadores_luminosos_plano_externo_interno_irradiado(element_1=[0],element_2=[0]):
    try:
        operacion = float(element_1[0])+float(element_2[0])
        tolerancia =True
        redondear = round(operacion,2)
        
        if(redondear <= 2):
            tolerancia = True
        else:
            tolerancia = False


        estado = validacion([tolerancia])
        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":str(redondear)+" mm",
                    "estado":tolerancia
                }
            ],
            "tolerancia":"La distancia entre el plano indicado por las luces interna y externa y el plano de irradiación debe ser ≤ ±2 mm.",
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