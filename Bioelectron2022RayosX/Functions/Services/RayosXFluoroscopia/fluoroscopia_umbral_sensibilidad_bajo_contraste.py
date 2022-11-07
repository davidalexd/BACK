from Functions.Services.validacion import validacion

def fluoroscopia_umbral_sensibilidad_bajo_contraste(attribute_1=[0],attribute_2=[0]):
    resultado = {"data":[{"parametros":"","resultado":0,"condicion":""}],"tolerancia":""}
    ordenador = [0,1,2,3]
    tolerancia = True
    tolerancias = [4,3.5,2.7,1.9]
    Uc = []
    validar = []
    for x in ordenador:
        operacion = float(attribute_1[x])/float(attribute_2[x])
        redondear = round(operacion,2)

        
        if(redondear <= tolerancias[x]):
            tolerancia = True
        else:
            tolerancia = False

        validar.append(tolerancia)

        Uc.append({
            "parametros":"",
            "resultado":redondear+" %",
            "estado":tolerancia
        })
    
    estado = validacion(validar)
    
    resultado = {
        "condicion":"",
        "data":Uc,
        "tolerancia":"Tamaño de campo de 36 cm ≤ 4%, de 30 cm ≤ 3.5%, de 23 cm ≤ 2.7%, de 15 cm o inferiores ≤ 1.9%",
        "estado":estado
        }
        
    return resultado
    
