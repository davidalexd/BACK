def fluoroscopia_ortogonalidad_haz_rayos_x_receptor_imagen(element):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":"El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°."}
    redondear = round(float(element[0]),2)
    
    tolerancia = True
    if(redondear<=1.5):
        tolerancia = True
    else:
        tolerancia = False
        
    resultado = {
        "data":[
            {"parametros":"","resultado":str(redondear)+"º","condicion":tolerancia}
        ],
        "tolerancia":"El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°."
        }

    return resultado