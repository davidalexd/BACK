from Functions.Services.validacion import validacion

def fluoroscopia_coincidencia_campo_radiacion_area_visualizada_detector(element_1,element_2):
    try:
        operacion=(float(element_1[0])**2)/(float(element_2[0])**2)
        redondear = round(operacion,2)
        tolerancia = True
        if(redondear<=1.15):
            tolerancia = True
        else:
            tolerancia = False
            
        estado = validacion([tolerancia])

        resultado = {
            "condicion":"",
            "data":[
                {
                    "parametros":"",
                    "resultado":redondear,
                    "estado":tolerancia
                }
            ],
            "tolerancia":"La relación entre el área del campo de radiación y el área visualizada en la superficie de entrada del detector de imagen debe ser ≤ 1.15",
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