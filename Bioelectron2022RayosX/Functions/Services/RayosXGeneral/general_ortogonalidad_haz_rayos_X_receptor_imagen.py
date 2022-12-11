from Functions.Services.validacion import validacion

def general_ortogonalidad_haz_rayos_X_receptor_imagen(element=[0]):
    # element = Valor de Angulación: 
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}

    redondear = round(float(element[0]),2)
    toleracia  = True
    
    if(redondear <= 1.5):
        toleracia  = True
    else:
        toleracia  = False

    estado = validacion([toleracia])
    resultado = {
        "condicion":"",
        "data":[
            {
                "parametros":"",
                "resultado":redondear,
                "estado":toleracia
            }
        ],
        "tolerancia":"El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°",
        "estado":estado
        }
    
    return resultado
