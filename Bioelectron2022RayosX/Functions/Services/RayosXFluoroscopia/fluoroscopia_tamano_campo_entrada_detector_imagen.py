from Functions.Services.validacion import validacion

def fluoroscopia_tamano_campo_entrada_detector_imagen(attributes_1=[0],attributes_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":"El ángulo que forman el eje central del haz de rayos X y el plano del receptor de imagen no deberá desviarse de los 90° más de 1.5°."}
    Uc = []
    validar = []
    tolerancia = True
    for x in range(len(attributes_1)):
        if (float(attributes_1[x])==0.0):
            valor_resultante = 0
        else:
            valor_resultante = float(attributes_2[x])/float(attributes_1[x])
        
        if (valor_resultante >= 0.85):
            tolerancia = True
        else:
            tolerancia = False


        redondear = round(valor_resultante,2)
        validar.append(tolerancia)
        Uc.append({
            "parametros":str(attributes_1[x])+" cm",
            "resultado":redondear,
            "estado":tolerancia
        })

    estado = validacion(validar) 

    resultado = {
        "condicion":"",
        "data":Uc,
        "tolerancia":"Para campos circulares: DM/DN ≥ 0.85. Para campos rectangulares sustituir el diámetro por la diagonal media.",
        "estado":estado
        }
    
    return resultado